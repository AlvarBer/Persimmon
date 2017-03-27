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
            touch.ud['dragging'] = True
            touch.ud['start_pin'] = self
            touch.ud['cur_line'] = Connection(start=self,
                                              start_pos=self.center,
                                              end=self, end_pos=self.center,
                                              color=self.color)
            self.parent.parent.parent.add_widget(touch.ud['cur_line'])
            #self.bind(pos=partial(lambda ins, val:)
            #self.bind(pos=partial(self.circle_bind,
            #                      circle=touch.ud['cur_line'].start))
            return True
        else:
            return False

    def circle_bind(self, pin, newpos, circle):
        print('on circle bind')
        circle = newpos

    def on_touch_up(self, touch):
        if ('dragging' in touch.ud.keys() and touch.ud['dragging'] and
            touch.button == 'left' and self.collide_point(*touch.pos)):
            touch.ud['cur_line'].end = self
            #touch.ud['cur_line'].dispatch('on_end')
            #print(touch.ud['cur_line'].end, touch.ud['cur_line'].end_pos)
            #self.bind(pos=partial(self.circle_bind,con=touch.ud['cur_line']))
            #del touch.ud['cur_line']
            return True
        else:
            return False

    """
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left' and 'dragging' in touch.ud.keys() and touch.ud['dragging']:
            touch.ud['dragging'] = False
            with self.canvas:
                Color(*self.color)
                touch.ud['end_circle'] = Ellipse(pos=self.pos, size=self.size)
            return True
        else:
            return False
    """
