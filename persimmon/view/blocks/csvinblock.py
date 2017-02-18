from persimmon.view.util import EmptyContent, CircularButton
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/csvinblock.kv')

class CSVInBlock(Block):
    out_1 = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pins.append(self.out_1)

    def pin_relative_position(self):
        return self.out_1.center
