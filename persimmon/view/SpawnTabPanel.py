from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from copy import deepcopy


kv = """
BoxLayout:
    orientation: 'vertical'
    TabbedPanel:
        size_hint_y: 20
        do_default_tab: False
        tab_width: '200dp'
        TabbedPanelItem:
            text: 'I/O'
            BoxLayout:
                spacing: '15dp'
                padding: '15dp'
                Button:
                    text: '.csv ->'
                Button:
                    text: '-> .csv'
        TabbedPanelItem:
            text: 'Estimators'
            BoxLayout:
                spacing: '15dp'
                padding: '15dp'
                Button:
                    text: 'Log reg'
                Button:
                    text: 'Rand Forest'
        TabbedPanelItem:
            text: 'Cross Validation'
            BoxLayout:
                spacing: '15dp'
                padding: '15dp'
                Button:
                    text: 'K-Folds'
    Label:
        size_hint_y: 80
        text: 'Content'
"""

class SpawnTabPanelApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    SpawnTabPanelApp().run()
