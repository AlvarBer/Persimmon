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
        self.predict_file = None

    def validate(self):
        result = backend.perform(pd.read_csv(self.train_file, header=0),
                                 self.estimator, self.cv)
        return '{:.3f}% (+/-{:.3f}%)'.format(result.mean() * 100,
                                             result.std() * 100)

    def predict(self):
        train_data = pd.read_csv(self.train_file, header=0)
        predict_data = pd.read_csv(self.predict_file, header=0)
        if predict_data.shape[1] == train_data.shape[1]:
            print('Removing last column')
            predict_data = predict_data.iloc[:, :-1]

        result = backend.perform(train_data, self.estimator, None,
                                 predict_data)
        return str(result)


class PrototypeScreen(BoxLayout):
    """PrototypeScreen is a pumped box layout used for the first iteration."""
    result = StringProperty()
    train_file = StringProperty()
    predict_file = StringProperty()

    def load_popup(self, string_property):
        print(string_property)
        popup = FileDialog(dir='~', filters=['*.csv'], size_hint=(0.8, 0.8))
        popup.bind(selected_file=partial(self.bind_strings,
                                         string_property=string_property))
        popup.open()

    def bind_strings(self, instance, value, string_property):
        """We are reeeally not supposed to do this, basically there is no easy
        way to get the property itself from the kv lang"""
        self.property(string_property).set(self, value)

    def on_train_file(self, instance, value):
        App.get_running_app().train_file = value

    def on_predict_file(self, instance, value):
        App.get_running_app().predict_file = value

    def validate(self):
        self.result = App.get_running_app().validate()

    def predict(self):
        self.result = App.get_running_app().predict()


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

