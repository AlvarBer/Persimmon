from persimmon.view.util import CircularButton, Connection
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line
from functools import partial


Builder.load_file('view/util/pin.kv')

class Pin(CircularButton):
    val = ObjectProperty(force_dispatch=True)
    block = ObjectProperty()
    ellipse = ObjectProperty()
    line = ObjectProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left':
            print('Creating connection')
            touch.ud['dragging'] = True
            touch.ud['start_pin'] = self
            touch.ud['cur_line'] = Connection(start=self,
                                              end=self,
                                              color=self.color)
            # Add to blackboard
            self.parent.parent.parent.add_widget(touch.ud['cur_line'])
            return True
        else:
            return False

    def circle_bind(self, pin, newpos, circle):
        print('on circle bind')
        circle = newpos

    def on_touch_up(self, touch):
        if ('dragging' in touch.ud.keys() and touch.ud['dragging'] and
            touch.button == 'left' and self.collide_point(*touch.pos)):
            print('Establishing connection')
            touch.ud['cur_line'].rebind_end(self)
            return True
        else:
            return False

