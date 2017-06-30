from persimmon.view.pins import OutputPin
from persimmon.view.blocks.block import Block  # MYPY HACK

from kivy.properties import ObjectProperty
from kivy.lang import Builder

from sklearn.neighbors import KNeighborsClassifier


Builder.load_file('persimmon/view/blocks/knnblock.kv')

class KNNBlock(Block):
    est_out = ObjectProperty()

    def function(self):
        self.est_out.val = KNeighborsClassifier()
