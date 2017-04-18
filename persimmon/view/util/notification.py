from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.clock import Clock


Builder.load_file('view/util/notification.kv')

class Notification(Popup):
    message = StringProperty()
    n_label = ObjectProperty()
    
    def on_message(self, instance, value):
        if self.n_label:
            print(self.n_label.size)
            print(self.size)

