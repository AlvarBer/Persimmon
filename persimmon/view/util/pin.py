from persimmon.view.util import CircularButton
from kivy.properties import ObjectProperty

from kivy.lang import Builder


Builder.load_file('view/util/pin.kv')

class Pin(CircularButton):
    val = ObjectProperty(force_dispatch=True)
    #parent = ObjectProperty()

