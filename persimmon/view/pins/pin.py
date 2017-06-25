from persimmon.view.pins.circularbutton import CircularButton  # MYPY HACK
from persimmon.view.util import Type, AbstractWidget, Connection
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line
from kivy.input import MotionEvent
from abc import abstractmethod

Builder.load_file('persimmon/view/pins/pin.kv')

class Pin(CircularButton, metaclass=AbstractWidget):
    val = ObjectProperty(None, force_dispatch=True)
    block = ObjectProperty()
    type_ = ObjectProperty(Type.ANY)

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
        elif self.type_ == Type.ANY or other.type_ == Type.ANY:
            return True  # Anything is possible with ANY
        else:
            return self.type_ == other.type_

    # Hack
    def on_type_(self, instance: 'Pin', value: Type):
        """ If the kv lang was a bit smarted this would not be needed
        """
        self.color = value.value
