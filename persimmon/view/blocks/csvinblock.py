from persimmon.view.util import OutputPin, FileDialog
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout

import pandas as pd


Builder.load_file('view/blocks/csvinblock.kv')

class CSVInBlock(Block):
    out_1 = ObjectProperty()
    file_chosen = StringProperty()
    file_dialog = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_dialog = FileDialog(dir='~', filters=['*.csv'],
                                      size_hint=(0.8, 0.8))
        # This binds two properties together
        self.file_dialog.bind(file_chosen=self.setter('file_chosen'))

    def function(self):
        if self.file_chosen:
            self.out_1.val = pd.read_csv(self.file_chosen, header=0)
        else:
            print('File not set!')

