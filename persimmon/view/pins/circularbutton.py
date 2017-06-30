from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.vector import Vector
from kivy.lang import Builder
from kivy.properties import ListProperty


Builder.load_file('persimmon/view/pins/circularbutton.kv')

class CircularButton(ButtonBehavior, Widget):
    color = ListProperty([.7, .7, .7])

    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

