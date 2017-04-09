from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Line
from functools import partial


"""
<Connection>:
    #lin: root.start_pos + root.end_pos
    canvas.after:
        Color:
            rgb: root.color
        Ellipse:
            pos: root.start_pos
            size: root.start.size
        Ellipse:
            pos: root.end_pos
            size: root.end.size
        #Line:
            #points: root.lin
"""

class Connection(Widget):
    start = ObjectProperty(allownone=True)
    end = ObjectProperty(allownone=True)
    color = ListProperty()
    lin = ObjectProperty()
    start_cr = ObjectProperty()
    end_cr = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.start:
            self.forward = True
            self.end = self.start
        else:
            self.forward = False
            self.start = self.end
        with self.canvas.before:
            Color(0.7, 0.7, 0.7)
            self.start_cr = Ellipse(pos=self.start.pos, size=self.start.size)
            Color(0.3, 0.3, 0.3)
            self.end_cr = Ellipse(pos=self.end.pos, size=self.end.size)
            Color(*self.color)
            self.lin = Line(points=self.start.center + self.end.center)
        self.start.fbind('pos', self.circle_bind, circle=self.start_cr)
        self.start.fbind('pos', self.line_bind_start)
        self.end.fbind('pos', self.circle_bind, circle=self.end_cr)
        self.end.fbind('pos', self.line_bind_end)

    def circle_bind(self, pin, val, circle):
        circle.pos = pin.pos

    def rebind_end(self, new_end):
        # Unbind previous end
        self.end.funbind('pos', self.circle_bind, circle=self.end_cr)
        self.end.funbind('pos', self.line_bind_end)
        # Changed end
        self.end = new_end
        # Put lastest value directly
        self.end_cr.pos = self.end.pos
        self.lin.points = self.lin.points[:2] + self.end.center
        # Rebind
        self.end.fbind('pos', self.circle_bind, circle=self.end_cr)
        self.end.fbind('pos', self.line_bind_end)

    def rebind_start(self, new_start):
        # Unbind previous end
        self.start.funbind('pos', self.circle_bind, circle=self.start_cr)
        self.start.funbind('pos', self.line_bind_start)
        # Changed end
        self.start = new_start
        # Put lastest value directly
        self.start_cr.pos = self.start.pos
        self.lin.points = self.start.center + self.lin.points[2:]
        # Rebind
        self.start.fbind('pos', self.circle_bind, circle=self.start_cr)
        self.start.fbind('pos', self.line_bind_start)

    def line_bind_start(self, pin, val):
        self.lin.points = pin.center + self.lin.points[2:]

    def line_bind_end(self, pin, val):
        self.lin.points = self.lin.points[:2] + pin.center

    def follow_cursor(self, newpos):
        if self.forward:
            self.lin.points = self.lin.points[:2] + [*newpos]
        else:
            self.lin.points = [*newpos] + self.lin.points[2:]

    def delete_connection(self, parent):
        parent.remove_widget(self)
        self.start.on_connection_delete(self)
        self.end.on_connection_delete(self)

    def on_touch_down(self, touch):
        if self.start.collide_point(*touch.pos):
            self.forward = False
            self.rebind_start(self.end)
            touch.ud['cur_line'] = self
            return True
        elif self.end.collide_point(*touch.pos):
            self.forward = True
            self.rebind_end(self.start)
            touch.ud['cur_line'] = self
            return True
        else:
            return False

    def warning(self):
        if self.color != (0.5, 0.5, 0.5):
            print('Redrawing')
            self.canvas.before.remove(self.lin)
            with self.canvas.before:
                Color(1, 0, 0)
                self.lin = Line(points=self.lin.points, width=1.1)
