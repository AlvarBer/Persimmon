from persimmon.view.util import Pin
from kivy.properties import ObjectProperty, ListProperty


class OutputPin(Pin):
    destinations = ListProperty()
