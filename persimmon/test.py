#!/usr/bin/env python3

import os
import kivy
kivy.require('1.9.0')
import pandas as pd
import backend
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
        print('Train file: {} |  Estimator: {}  | CV: {}'.format(self.train_file, self.estimator, self.cv))
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
    selected_train_file = ObjectProperty()

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
            App.get_running_app().train_file = selection[0]
            self._popup.dismiss()
            self.selected_train_file.text = selection[0]

    def validate(self):
        self.result = App.get_running_app().validate()


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

