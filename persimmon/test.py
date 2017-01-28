#!/usr/bin/env python3

import os
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

class TestApp(App):
    pass

class PrototypeScreen(BoxLayout):
    """ PrototypeScreen is a pumped box layout used for the first iteration """
    def load_popup(self):
        content = LoadDialog(load_func=self.load_file,
                             cancel_func=self.dismiss_popup)
        self._popup = Popup(title='Load file', content=content,
                            size_hint=(0.8, 0.8))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load_file(self, path, selection):
        if selection:
            print(os.path.join(path, selection[0]))


class LoadDialog(FloatLayout):
    cancel_func = ObjectProperty(None)
    load_func = ObjectProperty(None)
    load_button = ObjectProperty(None)
    selected_file = ObjectProperty(None)

    def file_selected(self, selection):
        if selection:
            filename = selection[0]
            self.load_button.disabled = False
        else:
            filename = ''
            self.load_button.disabled = True

        self.selected_file.text = filename


if __name__ == '__main__':
    TestApp().run()

