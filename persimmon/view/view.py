from kivy.app import App
# Widgets
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
# Properties
from kivy.properties import (ObjectProperty, NumericProperty, StringProperty,
                             ListProperty)
# Miscelaneous
from kivy.config import Config
from kivy.graphics import Color, Ellipse, Line, Rectangle, Bezier, SmoothLine
from kivy.core.window import Window
from functools import partial

from persimmon.view.blocks import (Block, SVMBlock, TenFoldBlock, CSVInBlock,
                                   CSVOutBlock, CrossValidationBlock)
from persimmon.view.util import CircularButton, EmptyContent

from collections import deque


Config.read('config.ini')

class ViewApp(App):
    background = ObjectProperty()

    def build(self):
        self.background = Image(source='connections.png').texture
        self.background.wrap = 'repeat'
        self.background.uvsize = 30, 30
        #self.background.uvsize = (Window.width / self.background.width,
        #                          Window.height / self.background.height)

class BlackBoard(ScatterLayout):
    blocks = ListProperty()
    initial_block = ObjectProperty()
    final_block = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dragging = False
        csv_in = CSVInBlock(pos=(25, 350))
        self.add_widget(csv_in)
        self.blocks.append(csv_in)
        self.initial_block = csv_in
        svm = SVMBlock(pos=(25, 250))
        self.add_widget(svm)
        self.blocks.append(svm)
        ten_fold = TenFoldBlock(pos=(25, 150))
        self.add_widget(ten_fold)
        self.blocks.append(ten_fold)
        cross_val = CrossValidationBlock(pos=(300, 250))
        self.add_widget(cross_val)
        self.blocks.append(cross_val)
        csv_out = CSVOutBlock(pos=(575, 250))
        self.add_widget(csv_out)
        self.blocks.append(csv_out)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.button =='left':
            block = self.in_block(*touch.pos)
            if block and block.in_pin(*touch.pos):
                self.dragging = True
                pin = block.in_pin(*touch.pos)
                with self.canvas:
                    Color(1, 1, 0)
                    touch.ud['start'] = Ellipse(pos=pin.pos, size=pin.size)
                    touch.ud['line'] = SmoothLine(points=(*pin.center, *touch.pos))
                touch.ud['start_block'] = block
                block.bind(pos=partial(self.circle_bind,
                                       circle=touch.ud['start'],
                                       pin=pin))
                touch.ud['start_pin'] = pin
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
        # TODO: Check if we are connecting forward or backwards
        if self.dragging and touch.button == 'left':
            self.dragging = False
            if self.collide_point(*touch.pos):
                block = self.in_block(*touch.pos)
                if block and block.in_pin(*touch.pos): # And block.collide_point
                    pin = block.in_pin(*touch.pos)
                    with self.canvas:
                        touch.ud['end'] = Ellipse(pos=pin.pos, size=pin.size)
                    start_block = touch.ud['start_block']
                    block.bind(pos=partial(self.circle_bind,
                                           circle=touch.ud['end'],
                                           pin=pin))
                    block.bind(pos=partial(self.line_bind,
                                           line=touch.ud['line'],
                                           pos_func=block.pin_relative_position,
                                           pin=pin))
                    start_block.bind(pos=partial(self.line_bind,
                                                 line=touch.ud['line'],
                                                 pos_func=start_block.pin_relative_position,
                                                 pin=touch.ud['start_pin'],
                                                 start=True))
                    pin.origin = touch.ud['start_pin']
                    return True
            self.canvas.remove(touch.ud['line'])
            self.canvas.remove(touch.ud['start'])
            return True
        else:
            return super().on_touch_up(touch)

    def execute_graph(self):
        queue = deque()
        seen = {}
        queue.extend(self.blocks)
        while queue:
            queque, seen = self.explore_graph(queue.popleft(), queue, seen)

    def explore_graph(self, block, queue: deque, seen: dict) -> (deque, dict):
        #print(f'Exploring {block.__class__}')
        for in_pin in block.input_pins:
            pin_uid = id(in_pin.origin)
            if pin_uid in seen:
                in_pin.val = seen[pin_uid]
            else:
                dependency = in_pin.origin.block
                if dependency in queue:
                    queue.remove(dependency)
                queue, seen = self.explore_graph(dependency, queue, seen)
        block.function()
        for out_pin in block.output_pins:
            seen[id(out_pin)] = out_pin.val
        #print(f'Explored {block.__class__}')
        return queue, seen



    def in_block(self, x, y):
        for block in self.blocks:
            if block.collide_point(x, y):
                return block
        return None

    def circle_bind(self, block, pos, circle, pin):
        circle.pos = pin.pos

    def line_bind(self, block, pos, line, pos_func, pin, start=False):
        if start:
            line.points = pos_func(pin) + line.points[2:]
        else:
            line.points = line.points[:2] + pos_func(pin)

if __name__ == '__main__':
    ViewApp().run()
