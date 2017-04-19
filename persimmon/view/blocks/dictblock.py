from persimmon.view.blocks import Block
from persimmon.view.util import OutputPin

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/dictblock.kv')

class DictBlock(Block):
    dict_out = ObjectProperty()
    string = StringProperty()
    tinput = ObjectProperty()

    def function(self):
        try:
            string = eval(self.tinput.text)
            if type(string) == dict:
                self.dict_out.val = string
        except Exception:
            self.dict_out.val = {}

