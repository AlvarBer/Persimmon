from persimmon.view.pins.pin import Pin  # MYPY HACK
from persimmon.view.util import Connection
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder
from kivy.graphics import Ellipse, Color

from kivy.input import MotionEvent

import logging


Builder.load_file('persimmon/view/pins/outpin.kv')
logger = logging.getLogger(__name__)

class OutputPin(Pin):
    destinations = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch: MotionEvent) -> bool:
        if (self.collide_point(*touch.pos) and touch.button == 'left' and
                not self.destinations):
            logger.info('Creating connection')
            touch.ud['cur_line'] = Connection(end=self,
                                              color=self.color)
            self.destinations.append(touch.ud['cur_line'])
            # Add to blackboard
            self.block.parent.parent.parent.connections.add_widget(touch.ud['cur_line'])
            self._circle_pin()
            return True
        else:
            return False

    def on_touch_up(self, touch: MotionEvent) -> bool:
        if ('cur_line' in touch.ud.keys() and touch.button == 'left' and
                self.collide_point(*touch.pos)):
            if (touch.ud['cur_line'].start and
                self.typesafe(touch.ud['cur_line'].start)):
                self.connect_pin(touch.ud['cur_line'])
                #logger.info('Establishing connection')
                #touch.ud['cur_line'].finish_connection(self)
                #self.destinations.append(touch.ud['cur_line'])
                #self._circle_pin()
            else:
                logger.info('Deleting connection')
                touch.ud['cur_line'].delete_connection()
            return True
        else:
            return False

    def on_connection_delete(self, connection: Connection):
        if connection in self.destinations:
            self.destinations.remove(connection)
            # Undoing circling
            self.funbind('pos', self._bind_circle)
            self.canvas.remove(self.circle)
            del self.circle
        else:
            logger.error('Deleting connection not fully formed')

    def connect_pin(self, connection):
        logger.info('Finish connection')
        connection.finish_connection(self)
        self.destinations.append(connection)
        self._circle_pin()

    def _circle_pin(self):
        if hasattr(self, 'circle'):
            logger.error('Circling pin twice')
            return
        with self.canvas:
            Color(*self.color)
            self.circle = Ellipse(pos=self.pos, size=self.size)
        self.fbind('pos', self._bind_circle)

    def _bind_circle(self, instance, value):
        self.circle.pos = self.pos
