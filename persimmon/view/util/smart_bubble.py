from kivy.uix.bubble import Bubble
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
import inspect
from persimmon.view import blocks


Builder.load_file('view/util/smart_bubble.kv')

class SmartBubble(Bubble):
    def __init__(self, backdrop, **kwargs):
        super().__init__(**kwargs)
        # Let's do some introspection, removing strings we do not care about
        block_members = map(lambda m: m[1], inspect.getmembers(blocks))
        classes = filter(lambda m: inspect.isclass(m) and
                         issubclass(m, blocks.Block) and
                         m.__class__ != blocks.Block, block_members)
        #print(list(map(lambda b: b.title, classes)))
        self.rv.data = [{'cls_name': b.__name__, 'cls_': b, 'bub': self,
                         'backdrop': backdrop} for b in classes]

    def dismiss(self):
        self.parent.remove_widget(self)

class FunList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'value': 'teeeest'}]

class Row(BoxLayout):
    cls_name = StringProperty()
    cls_ = ObjectProperty()
    bub = ObjectProperty()
    backdrop = ObjectProperty()

    def spawn_block(self):
        self.backdrop.add_widget(self.cls_())
        self.bub.dismiss()
