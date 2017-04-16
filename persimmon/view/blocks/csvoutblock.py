from persimmon.view.util import InputPin, FileDialog
from persimmon.view.blocks import Block

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder



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

    def function(self):
        if self.path:
            self.in_1.val.to_csv(path_or_buf=path)
        else:
            print('File not set!')
