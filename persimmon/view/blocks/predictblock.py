from persimmon.view.blocks.block import Block  # MYPY HACK
from persimmon.view.pins import InputPin, OutputPin
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('persimmon/view/blocks/predictblock.kv')

class PredictBlock(Block):
    est_in = ObjectProperty()
    data_in = ObjectProperty()
    plain_out = ObjectProperty()

    def function(self):
        self.plain_out.val = self.est_in.val.predict(self.data_in.val)


