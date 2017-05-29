from kivy.uix.bubble import Bubble
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from persimmon.view import blocks
from persimmon.view.util import InputPin, OutputPin
import inspect
import logging
from functools import reduce
from fuzzywuzzy import process
from kivy.core.window import Window


Builder.load_file('view/util/smart_bubble.kv')
logger = logging.getLogger(__name__)

class SmartBubble(Bubble):
    # TODO: cache instancing
    def __init__(self, backdrop, *, pin=None, **kwargs):
        super().__init__(**kwargs)
        self.y -= self.width
        #print(Window.size)
        self.pin = pin
        self.backdrop = backdrop
        # Let's do some introspection, removing strings we do not care about
        block_members = map(lambda m: m[1], inspect.getmembers(blocks))
        block_cls = filter(lambda m: inspect.isclass(m) and
                           issubclass(m, blocks.Block) and
                           m != blocks.Block, block_members)
        # Kivy properties are not really static, so we need to instance blocks
        instances = (block() for block in block_cls)
        if pin:  # Context sensitive if we are connecting
            instances = filter(self._is_suitable, instances)

        # This is how we pass information to each shown row
        self.rv.data = [{'cls_name': block.title, 'cls_': block.__class__,
                         'bub': self, 'backdrop': backdrop, 'pin': self.pin,
                         'block_pos': self.pos} for block in instances]
        self.cache = {data['cls_']: data['cls_name'] for data in self.rv.data}
        if self.backdrop.parent.hint:
            self.backdrop.parent.remove_hint()

    def on_touch_down(self, touch) -> bool:
        if not self.collide_point(*touch.pos):
            if self.pin:  # If there is a connection going on
                if issubclass(self.pin.__class__, InputPin) and self.pin.origin:
                    self.pin.origin.delete_connection()
                elif self.pin.destinations:
                    self.pin.destinations[-1].delete_connection()
            if touch.button == 'left':
                self.dismiss()
                self.backdrop.parent.add_hint()
                return True
            elif touch.button == 'right':
                self.x = touch.x
                self.y = touch.y - self.height
                return True
        else:
            return super().on_touch_down(touch)


    def dismiss(self):
        self.parent.remove_widget(self)

    def search(self, string):
        if string:
            results = process.extract(string, self.cache,
                                      limit=len(self.cache))
            self.rv.data = [{'cls_name': block[0], 'cls_': block[2],
                             'bub': self, 'backdrop': self.backdrop,
                             'pin': self.pin, 'block_pos': self.pos}
                            for block in results if block[1] > 50]
        else:
            self.rv.data = [{'cls_name': name, 'cls_': class_, 'bub': self,
                             'backdrop': self.backdrop, 'pin': self.pin,
                             'block_pos': self.pos}
                            for class_, name in self.cache.items()]

    def _is_suitable(self, block) -> bool:
        if issubclass(self.pin.__class__, InputPin):
            if any(filter(lambda p: p._type == self.pin._type,
                          block.output_pins)):
                return True
        else:
            if any(filter(lambda p: p._type == self.pin._type,
                          block.input_pins)):
                return True
        return False

class Row(BoxLayout):
    cls_name = StringProperty()
    cls_ = ObjectProperty()
    bub = ObjectProperty()
    backdrop = ObjectProperty()
    block_pos = ListProperty()
    pin = ObjectProperty(allownone=True)

    def spawn_block(self):
        block = self.cls_(pos=self.block_pos)
        self.backdrop.blocks.add_widget(block)
        if self.pin:
            if issubclass(self.pin.__class__, InputPin):
                other_pin = self._suitable_pin(block.output_pins)
                conn = self.pin.origin
            else:
                other_pin = self._suitable_pin(block.input_pins)
                conn = self.pin.destinations[-1]
            logger.debug('Spawning block {} from bubble'.format(block))
            other_pin.connect_pin(conn)
        self.bub.dismiss()

    def _suitable_pin(self, pins):
        return reduce(lambda p1, p2: p1 if p1._type == self.pin._type else p2,
                      pins)
