import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button

import os

# Classes for the popups
class LoadDialog(Popup):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class LR_Popup(Popup):
    pass

class MainScreen(FloatLayout):
    layout_content=ObjectProperty(None)
    algorithms_list = ObjectProperty(None)
    scroll_view_list = ObjectProperty(None)
    input_file = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))

    # Functions to add algorithms to the algorithms list
    def add_linear_reg(self):
        btn = Button(text="Linear Regression")
        self.algorithms_list.add_widget(btn, index=0)

    def add_logistic_regression(self):
        btn = Button(text="Logistic Regression")
        self.algorithms_list.add_widget(btn, index=0)

    def add_SVM(self):
        btn = Button(text="Support vector machine")
        self.algorithms_list.add_widget(btn, index=0)

    def add_K_means(self):
        btn = Button(text="K_means")
        self.algorithms_list.add_widget(btn, index=0)

    # General use functions for popups
    def dismiss_popup(self):
        self._popup.dismiss()

    # Load file popup functions
    def open_LoadFilePopup(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.7, 0.7))
        self._popup.open()

    def load(self, path, filename):
        self.dismiss_popup()

    #Open popups to change the parameters of concrete algorithm
    def open_LR_Popup(self):
        the_popup = LR_Popup()
        the_popup.open()

class proveApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    proveApp().run()
