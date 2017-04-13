from persimmon.view.blocks import Block
from persimmon.view.util import InputPin, OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/predictblock.kv')

class PredictBlock(Block):
    est_in = ObjectProperty()
    data_in = ObjectProperty()
    plain_out = ObjectProperty()
    
    def function(self):
        self.plain_out.val = self.est_in.val.predict(self.data_in.val)


