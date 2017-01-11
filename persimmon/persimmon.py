import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class MainScreen(FloatLayout):
    layout_content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

class FileView(Popup):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Persimmon(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    Persimmon().run()
