from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/block.kv')

class Block(DragBehavior, FloatLayout):
    block_color = ListProperty([1, 1, 1])
    block_label = StringProperty('label')
    inputs = ObjectProperty()
    outputs = ObjectProperty()
    block = ObjectProperty()
    input_pins = ListProperty()
    output_pins = ListProperty()

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

    def in_pin(self, x, y):
        for pin in self.input_pins + self.output_pins:
            if pin.collide_point(x, y):
                return pin
        return None

    def function(self):
        pass

    def pin_relative_position(self, pin):
        return pin.center

    def circle_bind(self, bind):
        pass

    def on_touch_down(self, touch):
        #print(f'{self.__class__} on touch down')
        pin = self.in_pin(*touch.pos)
        if pin:  # if touch is on pin let them handle
            return pin.on_touch_down(touch)
        else:  # else default behavior (drag if collide)
            return super().on_touch_down(touch)

    #def on_touch_up(self, touch):
        #result = super().on_touch_up(touch)
        #return result
