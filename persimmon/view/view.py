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
from kivy.graphics import Color, Ellipse, Line, Rectangle, Bezier
from kivy.core.window import Window
from functools import partial

from persimmon.view.blocks import (Block, SVMBlock, TenFoldBlock, CSVInBlock,
                                   CSVOutBlock, CrossValidationBlock,
                                   RandomForestBlock)
from persimmon.view.util import CircularButton, InputPin, OutputPin

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
        csv_in = CSVInBlock(pos=(15, 400))
        self.add_widget(csv_in)
        self.blocks.append(csv_in)
        self.initial_block = csv_in
        svm = SVMBlock(pos=(30, 310))
        self.add_widget(svm)
        self.blocks.append(svm)
        rf = RandomForestBlock(pos=(30, 215))
        self.add_widget(rf)
        self.blocks.append(rf)
        ten_fold = TenFoldBlock(pos=(15, 125))
        self.add_widget(ten_fold)
        self.blocks.append(ten_fold)
        cross_val = CrossValidationBlock(pos=(300, 250))
        self.add_widget(cross_val)
        self.blocks.append(cross_val)
        csv_out = CSVOutBlock(pos=(575, 250))
        self.add_widget(csv_out)
        self.blocks.append(csv_out)

    def on_touch_down(self, touch):
        # TODO: Refactor these three callbacks, maybe move onto pins itself?
        if self.collide_point(*touch.pos) and touch.button =='left':
            block = self.in_block(*touch.pos)
            if block:
                pin = block.in_pin(*touch.pos)
                if pin:
                    self.dragging = True
                    if ((issubclass(pin.__class__, InputPin) and pin.origin) or
                        (issubclass(pin.__class__, OutputPin) and pin.destinations)):
                        self.canvas.remove(pin.ellipse)
                        pin.unbind(pos=self.circle_bind)
                        touch.ud['line'] = pin.line
                        if issubclass(pin.__class__, InputPin):
                            pin.line.points = *pin.origin.pos, *pin.line.points[2:]
                            touch.ud['start_pin'] = pin.origin
                            touch.ud['start'] = pin.origin.ellipse
                            pin.origin = None
                            touch.ud['start_pin'].destinations.remove(pin)
                        else:
                            pin.line.points = *pin.destinations[0].pos, *pin.line.points[2:]
                            touch.ud['start_pin'] = pin.destinations[0]
                            touch.ud['start'] = pin.destinations[0].ellipse
                            touch.ud['start_pin'].origin = None
                            pin.destinations.remove(touch.ud['start_pin'])
                    else:
                        with self.canvas:
                            Color(*pin.color)
                            touch.ud['start'] = Ellipse(pos=pin.pos,
                                                        size=pin.size)
                            touch.ud['line'] = Line(points=(*pin.center,
                                                            *touch.pos))
                            touch.ud['start_pin'] = pin
                    return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.dragging:
            touch.ud['line'].points = [*touch.ud['line'].points[:-2], touch.x,
                                       touch.y]
            return True
        else:
            return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.dragging and touch.button == 'left':
            self.dragging = False
            if self.collide_point(*touch.pos):
                block = self.in_block(*touch.pos)
                if block:
                    pin = block.in_pin(*touch.pos)
                    if pin:
                        with self.canvas:
                            touch.ud['end'] = Ellipse(pos=pin.pos,
                                                      size=pin.size)
                        start_pin = touch.ud['start_pin']
                        start_block = start_pin.block
                        if issubclass(pin.__class__, InputPin):
                            pin.origin = start_pin
                            start_pin.destinations.append(pin)
                            touch.ud['line'].points = [*touch.pos,
                                                       *touch.ud['start_pin'].pos]
                        else:
                            start_pin.origin = pin
                            pin.destinations.append(start_pin)
                            touch.ud['line'].points = [*touch.ud['start_pin'].pos,
                                                       *touch.pos]
                        start_pin.bind(pos=partial(self.circle_bind,
                                             circle=touch.ud['start']))
                        pin.bind(pos=partial(self.circle_bind,
                                             circle=touch.ud['end']))
                        block.bind(pos=partial(self.line_bind,
                                               line=touch.ud['line'],
                                               pos_func=block.pin_relative_position,
                                               pin=pin))
                        start_block.bind(pos=partial(self.line_bind,
                                                     line=touch.ud['line'],
                                                     pos_func=start_block.pin_relative_position,
                                                     pin=start_pin))
                        start_pin.ellipse = touch.ud['start']
                        pin.ellipse = touch.ud['end']
                        pin.line = touch.ud['line']
                        start_pin.line = touch.ud['line']
                    return True
            self.canvas.remove(touch.ud['line'])
            self.canvas.remove(touch.ud['start'])
            return True
        else:
            return super().on_touch_up(touch)

    def execute_graph(self):
        queue = deque()
        seen = {}
        queue.append(self.blocks[0])
        while queue:
            queque, seen = self.explore_graph(queue.popleft(), queue, seen)

    def explore_graph(self, block, queue: deque, seen: dict) -> (deque, dict):
        #print(f'Exploring {block.__class__}')
        for in_pin in block.input_pins:
            pin_uid = id(in_pin.origin)
            if pin_uid not in seen:
                dependency = in_pin.origin.block
                if dependency in queue:
                    queue.remove(dependency)
                queue, seen = self.explore_graph(dependency, queue, seen)
            in_pin.val = seen[pin_uid]
        block.function()
        for out_pin in block.output_pins:
            seen[id(out_pin)] = out_pin.val
            for future_block in map(lambda x: x.block, out_pin.destinations):
                if future_block not in queue:
                    queue.append(future_block)

        #print(f'Explored {block.__class__}')
        return queue, seen

    def in_block(self, x, y):
        for block in self.blocks:
            if block.collide_point(x, y):
                return block
        return None

    def circle_bind(self, pin, pos, circle):
        circle.pos = pin.pos

    def line_bind(self, block, pos, line, pos_func, pin):
        if issubclass(pin.__class__, InputPin):
            line.points = pos_func(pin) + line.points[2:]
        else:
            line.points = line.points[:2] + pos_func(pin)


if __name__ == '__main__':
    ViewApp().run()
