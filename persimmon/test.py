#!/usr/bin/env python3

import os
import kivy
kivy.require('1.9.0')
import pandas as pd
import backend
from functools import partial
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty

class TestApp(App):
    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        self.train_file = None
        self.estimator = None
        self.cv = None
        self.predict_data = None

    def validate(self):
        result = backend.perform(pd.read_csv(self.train_file, header=0),
                                 self.estimator, self.cv, predict_data=None)
        return '{:.3f}% (+/-{:.3f}%)'.format(result.mean() * 100,
                                             result.std() * 100)

    def predict(self):
        backend.perform(pd.read_csv(self.train_file, header=0), self.estimator,
                        self.cv, predict_data=self.predict_data)


class PrototypeScreen(BoxLayout):
    """PrototypeScreen is a pumped box layout used for the first iteration."""
    result = StringProperty()
    text_input_train_file = StringProperty()

    def load_popup(self, tinput):
        content = FileDialog(dir='~', filters=['*.csv'],
                             size_hint=(0.8, 0.8))
        content.bind(selected_file=partial(self.change_file, text_input=tinput))
        content.open()

    def change_file(self, instance, value, text_input):
        self.text_input_train_file = value

    def on_text_input_train_file(self, instance, value):
        App.get_running_app().train_file = value

    def validate(self):
        self.result = App.get_running_app().validate()


class FileDialog(Popup):
    """File Dialogs is a popup that gets a file"""
    file_chooser = ObjectProperty()
    load_button = ObjectProperty()
    selected_file = StringProperty()

    def __init__(self, dir='~', filters=None,*args, **kwargs):
        super(FileDialog, self).__init__()
        self.file_chooser.path = dir
        if filters:
            self.file_chooser.filters=filters
        else:
            self.file_chooser.filters=[]


    def toggle_load_button(self, selection):
        if selection:
            self.load_button.disabled = False
        else:
            self.load_button.disabled = True


if __name__ == '__main__':
    TestApp().run()

