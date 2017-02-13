from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.widget import Widget


class ViewApp(App):
    pass

       
class Test(Widget):
    test_property = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('>>>>>>>>>>>')
        print(self.test_property)
        print('<<<<<<<<<<<')

if __name__ == '__main__':
    ViewApp().run()
