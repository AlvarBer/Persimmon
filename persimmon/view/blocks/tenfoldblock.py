from persimmon.view.util import EmptyContent, InputPin, OutputPin
from persimmon.view.blocks import Block

from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('view/blocks/tenfoldblock.kv')

class TenFoldBlock(Block):
    #in_1 = ObjectProperty()
    out_1 = ObjectProperty()

