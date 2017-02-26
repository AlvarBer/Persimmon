from persimmon.view.util import Pin
from kivy.properties import ObjectProperty


class InputPin(Pin):
    origin = ObjectProperty(allownone=True)
