from persimmon.view.blocks import Block
from persimmon.view.util import OutputPin

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/dictblock.kv')

class DictBlock(Block):
    dict_out = ObjectProperty()
    string = StringProperty()

    def function(self):
        try:
            self.dict_out.val = eval(self.string)
        except Exception:
            self.dict_out.val = {}

