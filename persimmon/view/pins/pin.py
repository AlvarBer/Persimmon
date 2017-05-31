from persimmon.view.pins import CircularButton
from persimmon.view.util import Connection
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line
from kivy.input.motionevent import MotionEvent
from persimmon.view.util import Type, AbstractWidget
from abc import abstractmethod


Builder.load_file('view/pins/pin.kv')

class Pin(CircularButton, metaclass=AbstractWidget):
    val = ObjectProperty(None, force_dispatch=True)
    block = ObjectProperty()
    _type = ObjectProperty(Type.ANY)

    @abstractmethod
    def on_touch_down(self, touch: MotionEvent) -> bool:
        raise NotImplementedError

    @abstractmethod
    def on_touch_up(self, touch: MotionEvent) -> bool:
        raise NotImplementedError

    @abstractmethod
    def on_connection_delete(self, connection: Connection):
        raise NotImplementedError

    @abstractmethod
    def connect_pin(self, connection: Connection):
        raise NotImplementedError

    def typesafe(self, other: 'Pin') -> bool:
        """ Tells if a relation between two pins is typesafe. """
        if self.block == other.block or self.__class__ == other.__class__:
            return False
        elif self._type == Type.ANY or other._type == Type.ANY:
            return True  # Anything is possible with ANY
        else:
            return self._type == other._type

    # Hack
    def on__type(self, instance, value):
        """ If the kv lang was a bit smarted this would not be needed
        """
        self.color = value.value

