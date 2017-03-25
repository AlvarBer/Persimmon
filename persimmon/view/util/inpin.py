from persimmon.view.util import Pin
from kivy.properties import ObjectProperty


class InputPin(Pin):
    origin = ObjectProperty(allownone=True)

    """
    def on_touch_down(self, touch):
        touch.ud['dragging'] = True
        touch.ud['start_pin'] = self
        with self.canvas:
            Color(*pin.color)
            touch.ud['start_cicle'] = Ellipse(pos=self.pos,
                                              size=self.size)
            touch.ud['cur_line'] = Line(points=(*pin.center,
                                                *touch.pos))
    """
