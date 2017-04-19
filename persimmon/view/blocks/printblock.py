from persimmon.view.util import InputPin
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/printblock.kv')

class PrintBlock(Block):
    in_1 = ObjectProperty()

    def function(self):
        self.parent.parent.parent.warning.title = 'Print results'
        self.parent.parent.parent.warning.message = str(self.in_1.val)
        self.parent.parent.parent.warning.open()
