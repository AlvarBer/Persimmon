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
from kivy.graphics import Color, Ellipse, Line, Rectangle, Bezier, SmoothLine
from kivy.core.window import Window
from kivy.vector import Vector
from functools import partial

from blocks import Block, SVMBlock, TenFoldBlock


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
        if self.collide_point(*touch.pos) and touch.button =='left':
            for block in self.blocks:
                if block.collide_point(*touch.pos):
                    if block.on_pin(*touch.pos):
                        self.dragging = True
                        with self.canvas:
                            Color(1, 1, 0)
                            touch.ud['start'] = Ellipse(pos=(touch.x - 15 / 2,
                                                             touch.y - 15 / 2),
                                                        size=(15, 15))
                            touch.ud['line'] = SmoothLine(points=(*touch.pos,
                                                                  *touch.pos))
                        block.bind(pos=partial(circle_start, touch=touch))
                        return True
                    else:
                        return super().on_touch_down(touch)
        else:
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.dragging:
            touch.ud['line'].points = (touch.ud['line'].points[:-2] +
                                       [touch.x, touch.y])
            return True
        else:
            return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.dragging and touch.button == 'left':
            self.dragging = False
            if self.collide_point(*touch.pos):
                for block in self.blocks:
                    if block.collide_point(*touch.pos):
                        if block.on_pin(*touch.pos):
                            with self.canvas:
                                Ellipse(pos=(touch.x - 15 / 2, touch.y - 15 / 2),
                                        size=(15, 15))
                            return True
            self.canvas.remove(touch.ud['line'])
            self.canvas.remove(touch.ud['start'])
            return True
        else:
            return super().on_touch_up(touch)

def circle_start(block, pos, touch):
    touch.ud['start'].pos = pos



class CircularButton(ButtonBehavior, Widget):

    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2


if __name__ == '__main__':
    ViewApp().run()
