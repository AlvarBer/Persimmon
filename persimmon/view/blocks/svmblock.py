from persimmon.view.pins import InputPin, OutputPin
from persimmon.view.blocks.block import Block  # MYPY HACK

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.svm import SVC


Builder.load_file('persimmon/view/blocks/svmblock.kv')

class SVMBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = SVC()
