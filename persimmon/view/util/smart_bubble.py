from kivy.uix.bubble import Bubble
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
import inspect
from persimmon.view import blocks
from persimmon.view.util import InputPin, OutputPin


Builder.load_file('view/util/smart_bubble.kv')

class SmartBubble(Bubble):
    # TODO: cache instancing
    def __init__(self, *, backdrop, pin=None, **kwargs):
        super().__init__(**kwargs)
        # Let's do some introspection, removing strings we do not care about
        block_members = map(lambda m: m[1], inspect.getmembers(blocks))
        block_cls = filter(lambda m: inspect.isclass(m) and
                           issubclass(m, blocks.Block) and
                           m != blocks.Block, block_members)
        #print(list(map(lambda b: b.title, classes)))
        block_cls = list(block_cls)
        suitable = []
        if pin:
            for block in block_cls:
                instance = block()
                if issubclass(pin, InputPin):
                    if any(filter(lambda p: p._type == pin._type,
                                  instance.input_pins)):
                        suitable.append(instance)
                else:
                    if any(filter(lambda p: p._type == pin._type,
                                  instance.input_pins)):
                        suitable.append(instance)
            self.rv.data = [{'cls_name': i.title, 'cls_': i.__class__,
                             'bub': self, 'backdrop': backdrop}
                             for i in suitable]
        else:
            self.rv.data = [{'cls_name': c.__name__, 'cls_': c,
                             'bub': self, 'backdrop': backdrop}
                            for c in block_cls]

    def on_touch_down(self, touch) -> bool:
        print('smubble touch down')
        if not self.collide_point(*touch.pos):
            print(touch.ud.keys())
            # HEY HEY HEY, this is a new touch event
            if 'cur_line' in touch.ud.keys():
                print(touch.ud['cur_line'])
            if touch.button == 'left':
                self.dismiss()
                return True
            elif touch.button == 'right':
                self.pos = touch.pos
                return True
        else:
            return super().on_touch_down(touch)

    def dismiss(self):
        self.parent.remove_widget(self)

class Row(BoxLayout):
    cls_name = StringProperty()
    cls_ = ObjectProperty()
    bub = ObjectProperty()
    backdrop = ObjectProperty()

    def spawn_block(self):
        self.backdrop.add_widget(self.cls_())
        self.bub.dismiss()
