from persimmon.view.pins.pin import Pin  # MYPY HACK
from persimmon.view.util import Connection
from kivy.lang import Builder
from kivy.graphics import Ellipse, Color
from kivy.properties import ObjectProperty
from kivy.input import MotionEvent
import logging


Builder.load_file('persimmon/view/pins/inpin.kv')
logger = logging.getLogger(__name__)

class InputPin(Pin):
    origin = ObjectProperty(allownone=True)

    # Kivy touch methods override
    def on_touch_down(self, touch: MotionEvent) -> bool:
        if (self.collide_point(*touch.pos) and touch.button == 'left' and
            not self.origin):
            logger.info('Creating connection')
            touch.ud['cur_line'] = Connection(start=self,
                                              color=self.color)
            self.origin = touch.ud['cur_line']
            # Add to blackboard
            self.block.parent.parent.parent.connections.add_widget(touch.ud['cur_line'])
            self._circle_pin()
            return True
        else:
            return False

    def on_touch_up(self, touch: MotionEvent) -> bool:
        if ('cur_line' in touch.ud.keys() and touch.button == 'left' and
                self.collide_point(*touch.pos)):
            if (touch.ud['cur_line'].end and
                self.typesafe(touch.ud['cur_line'].end)):
                self.connect_pin(touch.ud['cur_line'])
                #logger.info('Establishing connection')
                #touch.ud['cur_line'].finish_connection(self)
                #self.origin = touch.ud['cur_line']
                #self._circle_pin()
            else:
                logger.info('Deleting connection')
                touch.ud['cur_line'].delete_connection()
            return True
        else:
            return False

    def on_connection_delete(self, connection: Connection):
        if self.origin:
            self.origin = None
            # Undo pin circling
            self.funbind('pos', self._bind_circle)
            self.canvas.remove(self.circle)
            del self.circle
        else:
            logger.error('Deleting connection not fully formed')

    def connect_pin(self, connection):
        logger.info('Finish connection')
        connection.finish_connection(self)
        self.origin = connection
        self._circle_pin()

    def typesafe(self, other: Pin) -> bool:
        return super().typesafe(other) and self.origin == None

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

