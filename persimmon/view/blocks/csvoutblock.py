from persimmon.view.util import InputPin
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/csvoutblock.kv')

class CSVOutBlock(Block):
    in_1 = ObjectProperty()

    def function(self):
        print(self.in_1.val)
