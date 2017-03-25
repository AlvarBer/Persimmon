from persimmon.view.util import OutputPin
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty
from kivy.lang import Builder

import pandas as pd


Builder.load_file('view/blocks/csvinblock.kv')

class CSVInBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = pd.read_csv('iris.csv', header=0)
