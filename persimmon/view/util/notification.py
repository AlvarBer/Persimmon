from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.clock import Clock


Builder.load_file('view/util/notification.kv')

class Notification(Popup):
    message = StringProperty()

    """
    def on_message(self, instance, value):
        height = value.count('\n')
        width = max([len(x) for x in value.split('\n')])
        self.size = min(max(100, width * 10), 320), min(height * 18 + 100, 400)
    """

