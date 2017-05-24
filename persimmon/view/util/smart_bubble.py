from kivy.uix.bubble import Bubble
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
import inspect
from persimmon.view import blocks


Builder.load_file('view/util/smart_bubble.kv')

class SmartBubble(Bubble):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Let's do some introspection, removing strings we do not care about
        block_members = map(lambda m: m[1], inspect.getmembers(blocks))
        classes = filter(lambda m: inspect.isclass(m) and
                         issubclass(m, blocks.Block) and
                         m.__class__ != blocks.Block, block_members)
        #print(list(map(lambda b: b.title, classes)))
        self.rv.data = [{'cls_name': b.__name__} for b in classes]
        #self.rv.data = [{'cls_name': b.__name__, 'cls': b} for b in classes]

class FunList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'value': 'teeeest'}]

class Row(BoxLayout):
    #value = ObjectProperty()

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text=self.cls_name,
                               on_release=self._h))
    """
    def _h(self):
        print(type(self.cls))
