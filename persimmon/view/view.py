from kivy.app import App
# Widgets
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import DragBehavior, ButtonBehavior
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
# Properties
from kivy.properties import (ObjectProperty, NumericProperty, StringProperty,
                             ListProperty)
# Miscelaneous
from kivy.config import Config
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.vector import Vector


class ViewApp(App):
    background = ObjectProperty()

    def build(self):
        Config.read('config.ini')
        self.background = Image(source='background.png').texture
        self.background.wrap = 'repeat'
        self.background.uvsize = (Window.width / self.background.width,
                                  Window.height / self.background.height)


class BlackBoard(FloatLayout):
    blocks = ListProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dragging = False
        svm = SVMBlock(pos=(300, 200))
        self.add_widget(svm)
        self.blocks.append(svm)
        ten_fold = TenFoldBlock(pos=(550, 200))
        self.add_widget(ten_fold)
        self.blocks.append(ten_fold)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left':
            print('Blackboard pressed')
            for block in self.blocks:
                if block.collide_point(*touch.pos):
                    super().on_touch_down(touch)
                    break
            else:
                self.dragging = True
                with self.canvas:
                    Color(1, 1, 0)
                    d = 15
                    Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                    touch.ud['line'] = Line(points=(touch.pos))
        else:
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.dragging:
            with self.canvas:
                touch.ud['line'].points += touch.pos
            return True
        else:
            return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.dragging:
            with self.canvas:
                d = 15
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            self.dragging = False
            return True
        else:
            return super().on_touch_up(touch)

class Block(DragBehavior, BoxLayout):
    block_color = ListProperty()
    block_label = StringProperty()
    content = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if not self.is_eyebolt(*touch.pos):
            return super().on_touch_down(touch)
        else:
            return True

    def is_eyebolt(self, x, y):
        return False

class SVMBlock(Block):
    eyebolts = ObjectProperty()

    def is_eyebolt(self, x, y):
        for pin in self.eyebolts.children:
            if pin.collide_point(x, y):
                return True
        else:
            return False

class TenFoldBlock(Block):
    def is_eyebolt(self, x, y):
        return False

class CircularButton(ButtonBehavior, Widget):
    x_size = NumericProperty()
    y_size = NumericProperty()
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

if __name__ == '__main__':
    ViewApp().run()
