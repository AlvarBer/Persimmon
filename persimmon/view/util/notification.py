from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty


Builder.load_file('persimmon/view/util/notification.kv')

class Notification(Popup):
    message = StringProperty()
    
