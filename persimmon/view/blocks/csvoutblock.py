from persimmon.view.util import InputPin, FileDialog
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
import numpy as np
import pandas as pd


Builder.load_file('view/blocks/csvoutblock.kv')

class CSVOutBlock(Block):
    in_1 = ObjectProperty()
    path = StringProperty()
    file_dialog = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_dialog = FileDialog(dir='~', filters=['*.csv'],
                                      size_hint=(0.8, 0.8))
        # Let's bind two together
        self.file_dialog.bind(file_chosen=self.setter('path'))
        self.tainted = True
        self.tainted_msg = 'File not chosen in block {}!'.format(self.block_label)


    def function(self):
        if type(self.in_1.val) == np.ndarray:
            self.in_1.val = pd.DataFrame(self.in_1.val)
        self.in_1.val.to_csv(path_or_buf=self.path, index=False)

    def on_path(self, instance, value):
        if value != '':
            self.tainted = False
        else:
            self.tainted = True
