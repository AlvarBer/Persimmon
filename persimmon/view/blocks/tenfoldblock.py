from blocks import Block

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/tenfoldblock.kv')

class TenFoldBlock(Block):
    eyebolts = ObjectProperty()

    def on_pin(self, x, y):
        for pin in self.eyebolts.children:
            if pin.collide_point(x, y):
                return True
        else:
            return False
