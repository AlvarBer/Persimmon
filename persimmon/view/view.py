from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, ListProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.factory import Factory
from kivy.config import Config


class ViewApp(App):
    background = ObjectProperty()

    def __init__(self, *args, **kwargs):
        Config.read('config.ini')
        super().__init__(*args, **kwargs)
        self.background = Image(source='background.png').texture
        self.background.wrap = 'repeat'
        x = Window.width / self.background.width
        y = Window.height / self.background.height
        self.background.uvsize = (x, y)


class BlackBoard(FloatLayout):
    blocks = ListProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dragging = False
        svm = SVMBlock(pos=(300, 200), block_label='SVM',
                        block_color=(.478, .624, .208, 1))
        svm.add_widget(Factory.EmptyContent())
        self.add_widget(svm)
        self.blocks.append(svm)
        ten_fold = Block(pos=(550, 200), block_label='10-fold',
                         block_color=(.133, .40, .40, 1))
        ten_fold.add_widget(Factory.EmptyContent())
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

        return True

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

    def on_touch_down(self, touch):
        if not self.is_connection(*touch.pos):
            return super().on_touch_down(touch)
        else:
            return True

    def is_connection(self, x, y):
        return False

class SVMBlock(Block):
    x_pos = NumericProperty()
    y_pos = NumericProperty()

    def is_connection(self, x, y):
        print(self.pos)
        return False

if __name__ == '__main__':
    ViewApp().run()
