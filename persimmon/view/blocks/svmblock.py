from persimmon.view.util import InputPin, OutputPin
from persimmon.view.blocks import Block

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.svm import SVC


Builder.load_file('view/blocks/svmblock.kv')

class SVMBlock(Block):
    title2 = 'gds'
    out_1 = ObjectProperty()
    
    def function(self):
        self.out_1.val = SVC()
