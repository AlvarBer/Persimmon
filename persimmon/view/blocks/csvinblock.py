from persimmon.view.pins import OutputPin
from persimmon.view.util import FileDialog
from persimmon.view.blocks.block import Block  # MYPY HACK

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

import pandas as pd


Builder.load_file('persimmon/view/blocks/csvinblock.kv')

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
        self.tainted = True
        self.tainted_msg = 'File not chosen in block {}!'.format(self.title)

    def function(self):
        self.out_1.val = pd.read_csv(self.file_chosen, header=0)

    def on_file_chosen(self, instance, value):
        self.tainted = not value.endswith('.csv')
