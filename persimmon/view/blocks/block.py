# Persimmon stuff
from persimmon.view.util import Type, BlockType, AbstractWidget
from persimmon.view.pins import Pin, InputPin, OutputPin
# kivy stuff
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior, FocusBehavior
from kivy.properties import (ListProperty, StringProperty,
                             ObjectProperty, ObservableList)
from kivy.lang import Builder
from kivy.graphics import BorderImage, Color
from kivy.uix.image import Image
import logging
# Types are fun
from kivy.input import MotionEvent
from kivy.core.window import Window
from typing import Optional, Tuple
from abc import abstractmethod


logger = logging.getLogger()
Builder.load_file('persimmon/view/blocks/block.kv')

class Block(DragBehavior, FocusBehavior,
            FloatLayout, metaclass=AbstractWidget):
    block_color = ListProperty([1, 1, 1])
    title = StringProperty()
    label = ObjectProperty()
    inputs = ObjectProperty()
    outputs = ObjectProperty()
    input_pins = ListProperty()
    output_pins = ListProperty()
    t = ObjectProperty(Type)
    b = ObjectProperty(BlockType)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Reverse ids on class because dict ordering is reversed
        ids = list(self.ids.values())[::-1]
        self.input_pins = [x.__self__ for x in ids
                           if issubclass(x.__class__, InputPin)]
        self.output_pins = [x.__self__ for x in ids
                            if issubclass(x.__class__, OutputPin)]

        for pin in self.input_pins:
            pin.block = self
            self.gap = pin.width * 2
        for pin in self.output_pins:
            pin.block = self
            self.gap = pin.width * 2

        self.tainted_msg = 'Block {} has unconnected inputs'.format(self.title)
        self._tainted = False
        self.kindled = None
        self.border_texture = Image(source='persimmon/border.png').texture
        # Make block taller if necessary
        self.height = (max(len(self.output_pins), len(self.input_pins), 3) *
                       self.gap + self.label.height)
        # Position pins nicely
        #y_origin = self.y + (self.height - self.label.height)
        for i, in_pin in enumerate(list(self.input_pins[::-1]), 1):
            self._bind_pin(self, (in_pin.x, in_pin.y), in_pin, i, False)
            self.fbind('pos', self._bind_pin, pin=in_pin, i=i, output=False)
        for i, out_pin in enumerate(list(self.output_pins[::-1]), 1):
            self._bind_pin(self, (out_pin.x, out_pin.y), out_pin, i, True)
            self.fbind('pos', self._bind_pin, pin=out_pin, i=i, output=True)

    @property
    def tainted(self):
        # TODO: Check for orphanhood is not necessary
        return (self._tainted or (not self.is_orphan() and
                any(in_pin.origin == None for in_pin in self.input_pins)))

    @tainted.setter
    def tainted(self, value):
        self._tainted = value

    def is_orphan(self) -> bool:
        """ Tells if a block is orphan, i.e. whether it has any connection """
        for in_pin in self.input_pins:
            if in_pin.origin:
                return False
        for out_pin in self.output_pins:
            if out_pin.destinations:
                return False
        return True

    def in_pin(self, x: float, y: float) -> Optional[Pin]:
        """ Checks if a position collides with any of the pins in the block.
        """
        for pin in self.input_pins + self.output_pins:
            if pin.collide_point(x, y):
                return pin
        return None

    @abstractmethod
    def function(self):
        raise NotImplementedError

    # Kivy touch events override
    def on_touch_down(self, touch: MotionEvent) -> bool:
        pin = self.in_pin(*touch.pos)
        if pin:  # if touch is on pin let them handle
            return pin.on_touch_down(touch)
        else:  # else default behavior (drag if collide)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch: MotionEvent) -> bool:
        pin = self.in_pin(*touch.pos)
        if pin:
            result = pin.on_touch_up(touch)
        else:
            result = super().on_touch_up(touch)
        return result

    def kindle(self):
        """ Praise the sun \[T]/ """
        with self.canvas.before:
            Color(1, 1, 1)
            self.kindled = BorderImage(pos=(self.x - 2, self.y - 2),
                                       size=(self.width + 4,
                                             self.height + 4),
                                       texture=self.border_texture)
            self.fbind('pos', self._bind_border)

    def unkindle(self):
        """ Reverts the border image. """
        if self.kindled:
            self.canvas.before.remove(self.kindled)
            self.funbind('pos', self._bind_border)
            self.kindled = None
        else:
            logger.warning('Called unkindle on a block not kindled')

    # Auxiliary functions
    def _bind_border(self, block: 'Block', new_pos: Tuple[float, float]):
        """ Bind border to position. """
        self.kindled.pos = new_pos[0] - 2, new_pos[1] - 2

    def _bind_pin(self, block: 'Block', new_pos: Tuple[float, float],
                  pin: Pin, i: int, output: bool):
        """ Keep pins on their respective places. """
        pin.y = (block.y + (block.height - block.label.height) - i * self.gap +
                 pin.height / 2)
        if output:
            pin.x = block.x + block.width - self.gap
        else:
            pin.x = block.x + 5

    def on_focus(self, instance: 'Block', focus: bool):
        if focus:
            self.kindle()
        else:
            self.unkindle()

    def keyboard_on_key_down(self, window: Window, keycode: Tuple[int, str],
                             text: str, modifiers: ObservableList):
        if keycode == (127, 'delete'):
            for pin in self.input_pins:
                if pin.origin:
                    pin.origin.delete_connection()
            for pin in self.output_pins:
                for con in pin.destinations:
                    con.delete_connection()
            self.parent.remove_widget(self)
