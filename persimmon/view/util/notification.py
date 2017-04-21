from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty


Builder.load_file('view/util/notification.kv')

class Notification(Popup):
    message = StringProperty()
    n_label = ObjectProperty()
    
    def __init__(self, **kwargs):
        print('Creating popup')
        super().__init__(**kwargs)

    def on_message(self, instance, value):
        if self.n_label:
            pass
    
    def open(self):
        print('Opening popup')
        super().open()
