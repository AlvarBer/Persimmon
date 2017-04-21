from kivy.app import App
# Widgets
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
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

from persimmon.view.blocks import (SVMBlock, TenFoldBlock, CSVInBlock,
                                   CSVOutBlock, CrossValidationBlock,
                                   RandomForestBlock, GridSearchBlock,
                                   PredictBlock)
from persimmon.view.util import (CircularButton, InputPin, OutputPin,
                                 Notification)

from collections import deque
import persimmon.backend as backend
from kivy.lang import Builder


Config.read('config.ini')

class ViewApp(App):
    background = ObjectProperty()

    def build(self):
        self.background = Image(source='connections.png').texture
        self.background.wrap = 'repeat'
        self.background.uvsize = 30, 30
        #self.background.uvsize = (Window.width / self.background.width,
        #                          Window.height / self.background.height)
        return Builder.load_file('view/view.kv')

class BlackBoard(ScatterLayout):
    blocks = ObjectProperty()
    warning = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.warning = Notification(title='')

    def on_touch_move(self, touch):
        if touch.button == 'left' and 'cur_line' in touch.ud.keys():
            #print(self.get_root_window().mouse_pos)
            touch.ud['cur_line'].follow_cursor(touch.pos, self)
            return True
        else:
            return super().on_touch_move(touch)

    # TODO: Move dragging info into blackboard class instead of touch global
    def on_touch_up(self, touch):
        if self.disabled:
            return

        x, y = touch.x, touch.y
        # if the touch isnt on the widget we do nothing, just try children
        if not touch.grab_current == self:
            touch.push()
            touch.apply_transform_2d(self.to_local)
            for child in self.children:
                if child.dispatch('on_touch_up', touch):
                    touch.pop()
                    return True
            touch.pop()

        # remove it from our saved touches
        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)

        if ('cur_line' in touch.ud.keys() and touch.button == 'left'):
            print('Delete connection')
            touch.ud['cur_line'].delete_connection(self)
            return True

        # stop propagating if its within our bounds
        if self.collide_point(x, y):
            return True

    def in_block(self, x, y):
        for block in self.blocks.children:
            if block.collide_point(x, y):
                return block
        return None

    def see_relations(self):
        string = ''
        for block in self.blocks.children:
            if block.inputs:
                for pin in block.inputs.children:
                    if pin.origin:
                        string += '{} -> {}\n'.format(block.block_label,
                                                      pin.origin.end.block.block_label)
            if block.outputs:
                for pin in block.outputs.children:
                    for destination in pin.destinations:
                        string += '{} <- {}\n'.format(block.block_label,
                                                      destination.start.block.block_label)

        self.warning.title = 'Block Relations'
        self.warning.message = string
        self.warning.open()

    def to_ir(self):
        """ Transforms the relations between blocks into an intermediate
            representation in O(n), n being the number of pins. """
        ir_blocks = {}
        ir_inputs = {}
        ir_outputs = {}
        for block in self.blocks.children:
            block_hash = id(block)
            block_inputs, block_outputs = [], []
            avoid = False
            if block.inputs:
                print('irring fit')
                for pin in block.inputs.children:
                    print('block fit has {} children'.format(len(block.inputs.children)))
                    pin_hash = id(pin)
                    block_inputs.append(pin_hash)
                    if pin.origin:
                        other = id(pin.origin.end)
                    else:
                        avoid = True
                        break  # This means we are not connected
                    ir_inputs[pin_hash] = backend.InputEntry(origin=other,
                                                             pin=pin,
                                                             block=block_hash)
            if block.outputs and not avoid:
                for pin in block.outputs.children:
                    pin_hash = id(pin)
                    block_outputs.append(pin_hash)
                    dest = []
                    if pin.destinations:
                        for d in pin.destinations:
                            dest.append(id(d.start))
                    ir_outputs[pin_hash] = backend.OutputEntry(destinations=dest,
                                                       pin=pin,
                                                       block=block_hash)
            if not avoid:
                ir_blocks[block_hash] = backend.BlockEntry(inputs=block_inputs,
                                                        function=block.function,
                                                          outputs=block_outputs)
        self.outputs_hash = ir_outputs
        return backend.IR(blocks=ir_blocks, inputs=ir_inputs, outputs=ir_outputs)

    def process(self):
        tainted, tainted_msg = self.check_taint()
        if tainted:
            self.warning.title = 'Warning'
            self.warning.message = tainted_msg
            self.warning.open()
        else:
            backend.execute_graph(self.to_ir())

    # TODO: Merge this check with block tainted property
    def check_taint(self):
        for block in self.blocks.children:
            if block.inputs:
                orphaned = [x.origin == None for x in block.inputs.children]
                if not all(orphaned) and any(orphaned):
                    return True, 'Block "{}" has unconnected inputs!'.format(
                                    block.block_label)
            if block.tainted:
                return True, block.tainted_msg
        return False, ''

    def block_executed(self, block_hash):
        block = list(self.outputs_hash.keys()).index(block_hash)
        print(block)
        if block.outputs:
            for out_pin in block.outputs.children:
                for connection in block.outputs.destinations:
                    connection.pulse
                    Clock.schedule_once(lambda _: connection.stop_pulse, 5)

if __name__ == '__main__':
    ViewApp().run()
