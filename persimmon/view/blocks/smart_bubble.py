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

class SmartBubble(Bubble):
    rv = ObjectProperty()
    ti = ObjectProperty()

    # TODO: cache instancing
    def __init__(self, backdrop, pin: Optional[Pin] = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.y -= self.width  # type: ignore
        self.pin = pin
        self.backdrop = backdrop
        if pin:  # Context sensitive if we are connecting
            if issubclass(pin.__class__, InputPin):
                connection = pin.origin
            elif issubclass(pin.__class__, OutputPin):
                connection = pin.destinations[-1]
            else:
                raise AttributeError('Pin class where InPin or OutPin goes')
            connection.remove_info()
            suitable_blocks = filter(self._is_suitable, block_instances)
        else:
            suitable_blocks = block_instances
        # This is how we pass information to each shown row
        self.cache = {block.title: (block.__class__, block.block_color)
                      for block in suitable_blocks}
        Clock.schedule_once(lambda _: self._refocus(), 0.3)

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
            results = process.extract(string, self.cache.keys(),
                                      limit=len(self.cache))
            # First we filter results with more than 50 score and remove score
            blocks = [block_name for block_name, score in results if score > 50]
            available_blocks = [(name, (class_, color))
                                for name, (class_, color) in self.cache.items()
                                if name in blocks]
        else:
            # If there is no search we show all blocks
            available_blocks = self.cache.items()
        self.rv.data = [{'cls_name': name, 'cls_': class_, 'bub': self,
                         'backdrop': self.backdrop, 'pin': self.pin,
                         'block_pos': self.pos, 'block_color': color}
                        for name, (class_, color) in available_blocks]

    def _refocus(self):
        self.ti.focus = True

    def _is_suitable(self, block: blocks.Block) -> bool:
        return any((other_pin.typesafe(self.pin) for other_pin in
                    block.output_pins + block.input_pins))

class Row(BoxLayout):
    cls_name = StringProperty()
    cls_ = ObjectProperty()
    bub = ObjectProperty()
    backdrop = ObjectProperty()
    block_pos = ListProperty()
    pin = ObjectProperty(allownone=True)
    block_color = ObjectProperty()

    def spawn_block(self):
        block = self.cls_(pos=self.block_pos)
        self.backdrop.block_div.add_widget(block)
        if self.pin:
            if issubclass(self.pin.__class__, InputPin):
                other_pin = self._suitable_pin(block.output_pins)
                connection = self.pin.origin
            else:
                other_pin = self._suitable_pin(block.input_pins)
                connection = self.pin.destinations[-1]
            logger.debug('Spawning block {} from bubble'.format(block))
            other_pin.connect_pin(connection)
        self.bub.dismiss()

    def _suitable_pin(self, pins: List[Pin]) -> Pin:
        return reduce(lambda p1, p2: p1 if p1.type_ == self.pin.type_ else p2,
                      pins)

class ReTest(RecycleView):
    """ Because pyinstaller bug. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Block cache at module level
block_classes = inspect.getmembers(blocks, inspect.isclass)
# Let's do some introspection, removing strings we do not care about
# Kivy properties are not really static, so we need to instance blocks
# subclasses
block_instances = [member() for name, member in block_classes
                   if issubclass(member, blocks.Block) and
                       member != blocks.Block]
