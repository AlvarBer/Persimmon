# Kivy stuff
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Line, Point
from kivy.clock import Clock
# Numpy for sin
import numpy as np
# Others
from math import pi
import logging


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

logger = logging.getLogger(__name__)

class Connection(Widget):
    start = ObjectProperty(allownone=True)
    end = ObjectProperty(allownone=True)
    color = ListProperty()
    lin = ObjectProperty()
    start_cr = ObjectProperty()
    end_cr = ObjectProperty()

    def __init__(self, **kwargs):
        """ On this initializer the connection has to check whether the
        connection is being made forward or backwards. """
        super().__init__(**kwargs)
        if self.start:
            self.forward = True
            with self.canvas.before:
                Color(*self.color)
                self.start_cr = Ellipse(pos=self.start.pos,
                                        size=self.start.size)
                self.bez_start = self.start.center
                self.lin = Line(bezier=self.start.center * 4,
                                width=1.5)
            self._bind_pin(self.start)
        else:
            self.forward = False
            with self.canvas.before:
                Color(*self.color)
                self.end_cr = Ellipse(pos=self.end.pos, size=self.end.size)
                self.bez_end = self.end.center
                self.lin = Line(bezier=self.end.center * 4,
                                width=1.5)
            self._bind_pin(self.end)
        self.warned = False
        self.it = None

    def finish_connection(self, pin):
        """ This functions finishes a connection that has only start or end and
            is being currently dragged """
        if self.forward:
            self.end = pin
            with self.canvas.before:
                self.end_cr = Ellipse(pos=self.end.pos, size=self.end.size)
            self._bind_pin(self.end)
        else:
            self.start = pin
            with self.canvas.before:
                self.start_cr = Ellipse(pos=self.start.pos,
                                        size=self.start.size)
            self._bind_pin(self.start)

    # Kivy touch override
    def on_touch_down(self, touch):
        """ On touch down on connection means we are modifying an already
            existing connection, not creating a new one """
        if self.start.collide_point(*touch.pos):
            self.forward = False
            # Remove start edge
            self._unbind_pin(self.start)
            self.canvas.before.remove(self.start_cr)
            self.start_cr = None
            self.start.on_connection_delete(self)
            self.start = None
            # This signals that we are dragging a connection
            touch.ud['cur_line'] = self
            return True
        elif self.end.collide_point(*touch.pos):
            # Same as before but with the other edge
            self.forward = True
            self._unbind_pin(self.end)
            self.canvas.before.remove(self.end_cr)
            self.end_cr = None
            self.end.on_connection_delete(self)
            self.end = None
            touch.ud['cur_line'] = self
            return True
        else:
            return False

    def follow_cursor(self, newpos, blackboard):
        """ This functions makes sure the current end being dragged follows the
            cursor. It also checks for type safety and changes the line color
            if needed."""
        if self.forward:
            fixed_edge = self.start
            self.bez_end = [*newpos]
            self._rebezier()
        else:
            fixed_edge = self.end
            self.bez_start = [*newpos]
            self._rebezier()
        # The conditionals are so complicated because it is necessary to check
        # whether or not a pin in a block has been touched, and then check
        # the typesafety.
        if (self.warned and (not blackboard.in_block(*newpos) or
            not blackboard.in_block(*newpos).in_pin(*newpos) or
            blackboard.in_block(*newpos).in_pin(*newpos).typesafe(fixed_edge))):
            self._unwarn()
        elif (blackboard.in_block(*newpos) and
              blackboard.in_block(*newpos).in_pin(*newpos) and
              (not blackboard.in_block(*newpos).in_pin(*newpos).typesafe(fixed_edge))):
            # This conditional represents that the cursor stepped out the pin
            self._warn()

    def delete_connection(self, parent):
        """ This function deletes both ends (if they exist) and the connection
        itself. """
        parent.remove_widget(self)  # Self-destruct
        if self.start:
            self.start.on_connection_delete(self)
        if self.end:
            self.end.on_connection_delete(self)

    def pulse(self):
        """ Makes a connection appear to pulse by modifying its width
        continuosly. """
        self.it = self._change_width()
        next(self.it)
        Clock.schedule_interval(lambda _: next(self.it), 0.05) # 20 FPS

    def stop_pulse(self):
        """ Stops vibrating a connection. It will throw an execution if
        the connection is not pulsing right now. """
        self.it.throw(StopIteration)

    # Auxiliary methods
    # Binding methods
    def _unbind_pin(self, pin):
        """ Undos pin's circle and line binding. """
        pin.funbind('pos', self._circle_bind)
        pin.funbind('pos', self._line_bind)

    def _bind_pin(self, pin):
        """ Performs pin circle and line binding. """
        pin.fbind('pos', self._circle_bind)
        pin.fbind('pos', self._line_bind)

    def _circle_bind(self, pin, new_pos):
        if pin == self.start:
            self.start_cr.pos = pin.pos
        elif pin == self.end:
            self.end_cr.pos = pin.pos
        else:
            logger.error('No circle associated with pin')

    def _line_bind(self, pin, new_pos):
        if pin == self.start:
            self.bez_start = pin.center
            self._rebezier()
        elif pin == self.end:
            self.bez_end = pin.center
            self._rebezier()
        else:
            logger.error('No line associated with pin')

    # Pulsing methods
    def _change_width(self):
        """ Ok, so let me explain what is going on, this generator/coroutine
            changes the width of the line continuosly using the width_gen
            generator. We use it by calling it 20 times per second. The tricky
            part is stopping the scheduled calls. The way to tell Kivy to stop
            calling is to return a False value, and to do that we need to call
            this coroutine itself, which may be executing or not at that
            precise moment.

            That is where throw comes in, allowing for exceptions to be thrown
            on during the execution, hijacking the current execution (like a
            fast interruption), we need to return from this exception, in which
            we do not care about the value, and then return False on the
            regular execution in order to stop the calls."""
        try:
            for value in self._width_gen():
                self.lin.width = value
                yield
        except StopIteration:
            self.lin.width = 2
            yield
            yield False

    def _width_gen(self):
        """ Infinity oscillating generator (between 2 and 4) """
        val = 0
        while True:
            yield 2 * np.sin(val) + 4
            val += pi / 20

    # Warn methods
    def _warn(self):
        """ Changes the current line to a red thick connection. """
        self.warned = True
        self.canvas.before.remove(self.lin)
        with self.canvas.before:
            Color(1, 0, 0)
            self.lin = Line(points=self.lin.points, width=3)
        self._rebezier()

    def _unwarn(self):
        """ Returns the red thick connection to its normal state. """
        self.warned = False
        self.canvas.before.remove(self.lin)
        with self.canvas.before:
            Color(*self.color)
            self.lin = Line(points=self.lin.points, width=1.5)
        self._rebezier()

    # Bezier refreshing
    def _rebezier(self):
        """ Refreshes bezier curve according to start and end. """
        dist = (min(self.bez_start[0], self.bez_end[0]) +
                abs(self.bez_start[0] - self.bez_end[0]) / 2)
        self.lin.bezier = (self.bez_start + [dist, self.bez_start[1]] +
                           [dist, self.bez_end[1]] + self.bez_end)

