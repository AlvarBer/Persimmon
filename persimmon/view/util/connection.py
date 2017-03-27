from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Line


"""
<Connection>:
    lin: root.start_pos + root.end_pos
    canvas.after:
        Color:
            rgb: root.color
        Ellipse:
            pos: root.start_pos
            size: root.start.size
        Ellipse:
            pos: root.end_pos
            size: root.end.size
        Line:
            points: root.lin
"""

class Connection(Widget):
    start = ObjectProperty()
    end = ObjectProperty()
    start_pos = ListProperty()
    end_pos = ListProperty()
    color = ListProperty()
    lin = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.start_pos + self.end_pos)
        print(*self.start_pos, *self.end_pos)
        with self.canvas.before:
            Color(*self.color)
            self.start_cr = Ellipse(pos=self.start_pos, size=self.start.size)
            self.lin = Line(points=self.start_pos + self.end_pos)
        self.start.bind(pos=self.circle_bind)
        self.start.bind(pos=self.line_bind)
        self.end.bind(pos=self.circle_bind2)
        self.end.bind(pos=self.line_bind2)
        
    def circle_bind(self, pin, val):
        self.start_cr = pin.center

    def circle_bind2(self, pin, val):
        self.end_pos = pin.center
    
    def line_bind(self, pin, val):
        self.lin.points = pin.center + self.lin.points[2:]

    def line_bind2(self, pin, val):
        self.lin.points = self.lin.points[:2] + pin.center
    
    def follow_cursor(self, newpos):
        self.lin.points = self.lin.points[:2] + [*newpos]

