from persimmon.view.pins import InputPin
from persimmon.view.util import Notification
from persimmon.view.blocks.block import Block  # MYPY HACK
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('persimmon/view/blocks/printblock.kv')

class PrintBlock(Block):
    in_1 = ObjectProperty()

    def function(self):
        Notification(title='Print results',
                     message=str(self.in_1.val)).open()
