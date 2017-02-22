from persimmon.view.util import EmptyContent, InputPin, OutputPin
from persimmon.view.blocks import Block

from kivy.lang import Builder


Builder.load_file('view/blocks/crossvalidationblock.kv')

class CrossValidationBlock(Block):

    def function(self):
        pass
