from persimmon.view import blocks
from persimmon.view.pins import Pin, InputPin, OutputPin
from kivy.uix.bubble import Bubble
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty, ListProperty
import inspect
import logging
from functools import reduce
from fuzzywuzzy import process
from typing import List, Optional
from kivy.input import MotionEvent
from kivy.uix.recycleview import RecycleView


Builder.load_file('persimmon/view/blocks/smart_bubble.kv')
logger = logging.getLogger(__name__)

class ReTest(RecycleView):
    """ Because pyinstaller bug. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SmartBubble(Bubble):
    rv = ObjectProperty()
    ti = ObjectProperty()

    # TODO: cache instancing
    def __init__(self, backdrop, pin: Optional[Pin] = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.y -= self.width  # type: ignore
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
            if issubclass(pin.__class__, InputPin):
                conn = pin.origin
            elif issubclass(pin.__class__, OutputPin):
                conn = pin.destinations[-1]
            else:
                raise AttributeError('Pin class where InPin or OutPin goes')
            conn.remove_info()
            instances = filter(self._is_suitable, instances)

        # This is how we pass information to each shown row
        self.rv.data = [{'cls_name': block.title, 'cls_': block.__class__,
                         'bub': self, 'backdrop': backdrop, 'pin': self.pin,
                         'block_pos': self.pos} for block in instances]
        self.cache = {data['cls_']: data['cls_name'] for data in self.rv.data}
        Clock.schedule_once(self.refocus, 0.3)

    def refocus(self, _):
        self.ti.focus = True

    def on_touch_down(self, touch: MotionEvent) -> bool:
        if not self.collide_point(*touch.pos):
            if self.pin:  # If there is a connection going on
                if issubclass(self.pin.__class__, InputPin):
                    if self.pin.origin:
                        self.pin.origin.delete_connection()
                elif self.pin.destinations:
                    self.pin.destinations[-1].delete_connection()
            if touch.button == 'left':
                self.dismiss()
                return True
            elif touch.button == 'right':
                self.x = touch.x
                self.y = touch.y - self.height
                return True
        return super().on_touch_down(touch)

    def dismiss(self):
        self.parent.remove_widget(self)

    def search(self, string: str):
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

    def _is_suitable(self, block: blocks.Block) -> bool:
        return any(filter(lambda p: p.typesafe(self.pin),
                          block.output_pins + block.input_pins))

class Row(BoxLayout):
    cls_name = StringProperty()
    cls_ = ObjectProperty()
    bub = ObjectProperty()
    backdrop = ObjectProperty()
    block_pos = ListProperty()
    pin = ObjectProperty(allownone=True)

    def spawn_block(self):
        block = self.cls_(pos=self.block_pos)
        self.backdrop.block_div.add_widget(block)
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

    def _suitable_pin(self, pins: List[Pin]) -> Pin:
        return reduce(lambda p1, p2: p1 if p1.type_ == self.pin.type_ else p2,
                      pins)
