#!/usr/bin/env python3

import os
import kivy
kivy.require('1.9.0')
import pandas as pd
import backend
from functools import partial, partialmethod
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
    """ PrototypeScreen is a pumped box layout used for the first iteration """
    result = StringProperty()
    text_input_train_file = StringProperty()

    def load_popup(self, tinput):
        content = LoadDialog(size_hint=(0.8, 0.8))
        content.bind(selected_file=partial(self.callback, text_input=tinput))
        content.open()

    def callback(self, instance, value, text_input):
        text_input.text = value

    def on_text_input_train_file(self, instance, value):
        App.get_running_app().train_file = value
        print(App.get_running_app().train_file)

    def validate(self):
        self.result = App.get_running_app().validate()


class LoadDialog(Popup):
    load_button = ObjectProperty(None)
    selected_file = StringProperty(None)

    def toggle_load_button(self, selection):
        if selection:
            filename = selection[0]
            self.load_button.disabled = False
        else:
            filename = ''
            self.load_button.disabled = True


if __name__ == '__main__':
    TestApp().run()

