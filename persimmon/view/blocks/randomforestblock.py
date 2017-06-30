from persimmon.view.pins import OutputPin
from persimmon.view.blocks.block import Block  # MYPY HACK

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.ensemble import RandomForestClassifier


Builder.load_file('persimmon/view/blocks/randomforestblock.kv')

class RandomForestBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = RandomForestClassifier()
