from persimmon.view.util import CircularButton
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line


Builder.load_file('view/util/pin.kv')

class Pin(CircularButton):
    val = ObjectProperty(force_dispatch=True)
    block = ObjectProperty()
    ellipse = ObjectProperty()
    line = ObjectProperty()
    
    def on_touch_down(self, touch):
        #print(f'{self.__class__} on touch down')
        if self.collide_point(*touch.pos) and touch.button == 'left':
            touch.ud['dragging'] = True
            touch.ud['start_pin'] = self

            with self.canvas:
                Color(*self.color)
                touch.ud['start_cicle'] = Ellipse(pos=self.pos,
                                                  size=self.size)
                touch.ud['cur_line'] = Line(points=(*self.center,
                                                    *touch.pos))
            return True
        else:
            return False

    def on_touch_move(self, touch):
        print(f'{self.parent.parent.__class__} on touch move')
        if (touch.button == 'left' and 'dragging' in touch.ud.keys() and
            touch.ud['dragging']):
            touch.ud['cur_line'].points = (*touch.ud['cur_line'].points[:-2],
                                           *touch.pos)
            return True
        else:
            return False

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left' and 'dragging' in touch.ud.keys() and touch.ud['dragging']:
            touch.ud['dragging'] = False
            with self.canvas:
                Color(*self.color)
                touch.ud['end_circle'] = Ellipse(pos=self.pos, size=self.size)
            return True
        else:
            return False
