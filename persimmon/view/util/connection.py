# Kivy stuff
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
# For type hinting
from kivy.input import MotionEvent
from typing import Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from persimmon.view.pins.pin import Pin  # MYPY HACK
import numpy as np
# Others
from math import pi
import logging


#TODO: Info must be before everything
Builder.load_string("""
<Connection>:

<Info>:
    #pos: self.pos
    text: 'Spawn new block'
    font_size: '15dp'
    size_hint: None, None
    size: self.texture_size
    color: 1, 1, 1, 0.7
    padding: 5, 5
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.7
        Rectangle:
            pos: self.pos
            size: self.texture_size
""")
logger = logging.getLogger(__name__)

class Info(Label):
    pass

class Connection(Widget):
    start = ObjectProperty(allownone=True)
    end = ObjectProperty(allownone=True)
    color = ListProperty()
    lin = ObjectProperty()

    def __init__(self, **kwargs):
        """ On this initializer the connection has to check whether the
        connection is being made forward or backwards. """
        super().__init__(**kwargs)
        if self.start:
            self.forward = True
            # The value is repeated for correctness sake
            self.bez_start, self.bez_end = [self.start.center] * 2
            with self.canvas.before:
                Color(*self.color)
                self.lin = Line(bezier=self.bez_start * 4, width=1.5)
            self._bind_pin(self.start)
        else:
            self.forward = False
            self.bez_start, self.bez_end = [self.end.center] * 2
            with self.canvas.before:
                Color(*self.color)
                self.lin = Line(bezier=self.bez_end * 4, width=1.5)
            self._bind_pin(self.end)
        self.warned = False
        self.info = Factory.Info(pos=self.bez_start)
        Window.add_widget(self.info)

    def finish_connection(self, pin: 'Pin'):
        """ This functions finishes a connection that has only start or end and
            is being currently dragged """
        self.remove_info()
        if self.forward:
            self.end = pin
            self._bind_pin(self.end)
        else:
            self.start = pin
            self._bind_pin(self.start)

    # Kivy touch override
    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ On touch down on connection means we are modifying an already
            existing connection, not creating a new one. """
        # TODO: remove start check?
        if self.start and self.start.collide_point(*touch.pos):
            self.forward = False
            # Remove start edge
            self._unbind_pin(self.start)
            self.start.on_connection_delete(self)
            self.start = None
            # This signals that we are dragging a connection
            touch.ud['cur_line'] = self
            Window.add_widget(self.info)
            return True
        elif self.end and self.end.collide_point(*touch.pos):
            # Same as before but with the other edge
            self.forward = True
            self._unbind_pin(self.end)
            self.end.on_connection_delete(self)
            self.end = None
            touch.ud['cur_line'] = self
            Window.add_widget(self.info)
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
        self.info.pos = [*newpos]
        # The conditionals are so complicated because it is necessary to check
        # whether or not a pin in a block has been touched, and then check
        # the typesafety.
        if (self._in_pin(blackboard, newpos) and
            not self._in_pin(blackboard, newpos).typesafe(fixed_edge)):
            # This conditional represents that the cursor stepped out the pin
            self.info.text = 'Connection is not possible'
            self._warn()
        elif (self._in_pin(blackboard, newpos) and
              self._in_pin(blackboard, newpos).typesafe(fixed_edge)):
            self.info.text = 'Connect'
            if self.warned:
                self._unwarn()
        else:
            self.info.text = 'Spawn new block'
            if self.warned:
                self._unwarn()

    def delete_connection(self):
        """ This function deletes both ends (if they exist) and the connection
        itself. """
        self.parent.remove_widget(self)  # Self-destruct
        self.remove_info()
        if self.start:
            self._unbind_pin(self.start)
            self.start.on_connection_delete(self)
        if self.end:
            self._unbind_pin(self.end)
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

    def remove_info(self):
        Window.remove_widget(self.info)

    # Auxiliary methods
    def _in_pin(self, blackboard, pos):
        block = blackboard.in_block(*pos)
        if block:
            pin = block.in_pin(*pos)
            if pin:
                return pin
        return False

    # Binding methods
    def _unbind_pin(self, pin: 'Pin'):
        """ Undos pin's circle and line binding. """
        pin.funbind('pos', self._line_bind)

    def _bind_pin(self, pin: 'Pin'):
        """ Performs pin circle and line binding. """
        pin.fbind('pos', self._line_bind)
        self._line_bind(pin, pin.pos)

    def _line_bind(self, pin: 'Pin', new_pos: Tuple[float, float]):
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
            yield np.sin(val) + 3
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
        """ Refreshes bezier curve according to start and end.
        It uses the arctan to force the bèzier curve always going a bit
        forward before drifting."""
        arc_tan = np.arctan2(self.bez_start[1] - self.bez_end[1],
                             self.bez_start[0] - self.bez_end[0])
        abs_angle = np.abs(np.degrees(arc_tan))
        # We use the angle value plus a fixed amount to steer the line a bit
        start_right = [self.bez_start[0] - 5 - 0.6 * abs_angle,
                       self.bez_start[1]]
        end_left = [self.bez_end[0] + 5 + 0.6 * abs_angle, self.bez_end[1]]
        # Y distance to mid point
        dist = (min(self.bez_start[0], self.bez_end[0]) +
                abs(self.bez_start[0] - self.bez_end[0]) / 2)
        # This updates the bèzier curve graphics
        self.lin.bezier = (self.bez_start + start_right +
                           [dist, self.bez_start[1]] + [dist, self.bez_end[1]] +
                           end_left + self.bez_end)

    def _search_window(self):
        return Window
