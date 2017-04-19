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
            with self.canvas.before:
                Color(*self.color)
                self.start_cr = Ellipse(pos=self.start.pos,
                                        size=self.start.size)
                self.lin = Line(points=self.start.center + self.start.center,
                                width=1.5)
            self.start.fbind('pos', self.circle_bind)
            self.start.fbind('pos', self.line_bind)
        else:
            self.forward = False
            with self.canvas.before:
                Color(*self.color)
                self.end_cr = Ellipse(pos=self.end.pos, size=self.end.size)
                self.lin = Line(points=self.end.center + self.end.center,
                                width=1.5)
            self.end.fbind('pos', self.circle_bind)
            self.end.fbind('pos', self.line_bind)
        self.warned = False

    def finish_connection(self, pin):
        """ This functions finishes a connection that has only start or end and
            is being currently dragged """
        if self.forward:
            self.end = pin
            with self.canvas.before:
                self.end_cr = Ellipse(pos=self.end.pos, size=self.end.size)
            self.rebind_pin(self.end, pin)
        else:
            self.start = pin
            with self.canvas.before:
                self.start_cr = Ellipse(pos=self.start.pos,
                                        size=self.start.size)
            self.rebind_pin(self.start, pin)

    def follow_cursor(self, newpos, blackboard):
        """ This functions makes sure the current end being dragged follows the
            cursor """
        if self.forward:
            self.lin.points = self.lin.points[:2] + [*newpos]
            fixed_edge = self.start
            moving_edge = self.end
        else:
            self.lin.points = [*newpos] + self.lin.points[2:]
            fixed_edge = self.end
            moving_edge = self.start
        if self.warned:
            if (blackboard.in_block(*newpos) and
                blackboard.in_block(*newpos).in_pin(*newpos) and not
                fixed_edge.typesafe(blackboard.in_block(*newpos).in_pin(*newpos))):
                    return
            self.unwarn()
        else:
            if (blackboard.in_block(*newpos) and
                blackboard.in_block(*newpos).in_pin(*newpos) and (not
                fixed_edge.typesafe(blackboard.in_block(*newpos).in_pin(*newpos) or
                fixed_edge.block == blackboard.in_block(*newpos)))):
                self.warn()



    def delete_connection(self, parent):
        """ This function deletes both ends (if they exist) and the connection
            itself. """
        parent.remove_widget(self)
        if self.start:
            self.start.on_connection_delete(self)
        if self.end:
            self.end.on_connection_delete(self)

    def on_touch_down(self, touch):
        """ On touch down on connection means we are modifying an already
            existing connection, not creating a new one """
        if self.start.collide_point(*touch.pos):
            self.forward = False
            self.unbind_pin(self.start)
            self.uncircle_pin(self.start)
            self.start.on_connection_delete(self)
            touch.ud['cur_line'] = self
            self.start = None
            return True
        elif self.end.collide_point(*touch.pos):
            self.forward = True
            self.unbind_pin(self.end)
            self.uncircle_pin(self.end)
            self.end.on_connection_delete(self)
            touch.ud['cur_line'] = self
            self.end = None
            return True
        else:
            return False

    def rebind_pin(self, old, new):
        """ Unbinds pin and circle pin, changes pin and rebinds. """
        old.funbind('pos', self.circle_bind)
        old.funbind('pos', self.line_bind)
        old = new
        old.fbind('pos', self.circle_bind)
        old.fbind('pos', self.line_bind)


    def unbind_pin(self, finish):
        finish.funbind('pos', self.circle_bind)
        finish.funbind('pos', self.line_bind)

    def uncircle_pin(self, pin):
        if pin == self.start:
            self.canvas.before.remove(self.start_cr)
        elif pin == self.end:
            self.canvas.before.remove(self.end_cr)
        else:
            print('Attempted to uncircle pin without circle')

    def circle_bind(self, pin, new_pos):
        if pin == self.start:
            self.start_cr.pos = pin.pos
        elif pin == self.end:
            self.end_cr.pos = pin.pos
        else:
            print('No circle associated with pin')

    def line_bind(self, pin, new_pos):
        if pin == self.start:
            self.lin.points = pin.center + self.lin.points[2:]
        elif pin == self.end:
            self.lin.points = self.lin.points[:2] + pin.center
        else:
            print('No line associated with pin')

    def warn(self):
        self.warned = True
        self.canvas.before.remove(self.lin)
        with self.canvas.before:
            Color(1, 0, 0)
            self.lin = Line(points=self.lin.points, width=2)

    def unwarn(self):
        self.warned = False
        self.canvas.before.remove(self.lin)
        with self.canvas.before:
            Color(*self.color)
            self.lin = Line(points=self.lin.points, width=2)

