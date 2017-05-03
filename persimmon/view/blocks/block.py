# Persimmon stuff
from persimmon.view.util import Type, BlockType, Pin
# kivy stuff
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.graphics import BorderImage, Color
from kivy.uix.image import Image
# Types are fun
from typing import Optional


Builder.load_file('view/blocks/block.kv')

class Block(DragBehavior, FloatLayout):
    block_color = ListProperty([1, 1, 1])
    title = StringProperty()
    inputs = ObjectProperty()
    outputs = ObjectProperty()
    input_pins = ListProperty()
    output_pins = ListProperty()
    t = ObjectProperty(Type)
    b = ObjectProperty(BlockType)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.inputs:
            for pin in self.inputs.children:
                self.input_pins.append(pin)
                pin.block = self
        if self.outputs:
            for pin in self.outputs.children:
                self.output_pins.append(pin)
                pin.block = self
        self.tainted_msg = 'Block {} has unconnected inputs'.format(self.title)
        self._tainted = False
        self.kindled = None
        self.border_texture = Image(source='tex4.png').texture

    @property
    def tainted(self):
        return any(in_pin.origin == None for in_pin in self.input_pins) and not self.is_orphan()# and self._tainted

    @tainted.setter
    def tainted(self, value):
        self._tainted = value

    def in_pin(self, x: float, y: float) -> Optional[Pin]:
        """ Checks if a position collides with any of the pins in the block.
        """
        for pin in self.input_pins + self.output_pins:
            if pin.collide_point(x, y):
                return pin
        return None

    def function(self):
        pass

    def pin_relative_position(self, pin):
        return pin.center

    def on_touch_down(self, touch):
        pin = self.in_pin(*touch.pos)
        if pin:  # if touch is on pin let them handle
            return pin.on_touch_down(touch)
        else:  # else default behavior (drag if collide)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
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
            self.kindled = BorderImage(pos=(self.x - 5, self.y - 5),
                                       size=(self.width + 10,
                                             self.height + 10),
                                       texture=self.border_texture)
            self.fbind('pos', self.bind_border)

    def unkindle(self):
        """ Reverts the border image. """
        if self.kindled:
            self.canvas.before.remove(self.kindled)
            self.funbind('pos', self.bind_border)
            self.kindled = None
        else:
            logger.warning('Called unkindle on a block not kindled')

    def bind_border(self, block, new_pos):
        """ Bind border to position. """
        self.kindled.pos = new_pos[0] - 5, new_pos[1] - 5

    def is_orphan(self):
        for in_pin in self.input_pins:
            if in_pin.origin:
                return False
        for out_pin in self.output_pins:
            if out_pin.destinations:
                return False
        return True
