from persimmon.view.util import InputPin, Notification
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/printblock.kv')

class PrintBlock(Block):
    in_1 = ObjectProperty()

    def function(self):
        Notification(title='Print results',
                     message=str(self.in_1.val)).open()
