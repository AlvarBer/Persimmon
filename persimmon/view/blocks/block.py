from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import DragBehavior
from kivy.properties import ListProperty, StringProperty
from kivy.lang import Builder


Builder.load_file('view/blocks/block.kv')


class Block(DragBehavior, BoxLayout):
    block_color = ListProperty([1, 1, 1, 1])
    block_label = StringProperty('label')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_pin(self, x, y):
        return False

