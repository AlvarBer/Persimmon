import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button


#Classes for the popups
class LR_Popup(Popup):
    pass

class LoadDialog(Popup):
    pass

class MainScreen(FloatLayout):
    layout_content=ObjectProperty(None)
    algorithms_list = ObjectProperty(None)
    scroll_view_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))

    #Functions to add algorithms to the algorithms list
    def add_linear_reg(self):
        btn = Button(text="Linear Regression")
        self.algorithms_list.add_widget(btn,index=0)

    def add_logistic_regression(self):
        btn = Button(text="Logistic Regression")
        self.algorithms_list.add_widget(btn, index=0)

    def add_SVM(self):
        btn = Button(text="Support vector machine")
        self.algorithms_list.add_widget(btn, index=0)

    def add_K_means(self):
        btn = Button(text="K_means")
        self.algorithms_list.add_widget(btn, index=0)

    #Open the popup to select the input file
    def open_LoadFilePopup(self):
        the_popup = LoadDialog()
        the_popup.open()

    def close_LoadFilePopup(self):
        pass

    #Open popups to change the parameters of concrete algorithm
    def open_LR_Popup(self):
        the_popup = LR_Popup()
        the_popup.open()

class proveApp(App):
    def build(self):
        return MainScreen()

prove = proveApp()
prove.run()