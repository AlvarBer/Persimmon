# Persimmon imports
from persimmon.view import blocks
from persimmon.view.util import Notification
from persimmon.view.blocks import Block
import persimmon.backend as backend
# Kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.core.window import Window
# Kivy Widgets
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
# Others
from functools import partial, reduce
from collections import deque
import logging
from typing import Optional
from itertools import chain


logger = logging.getLogger(__name__)
Config.read('config.ini')

class ViewApp(App):
    background = ObjectProperty()

    def build(self):
        self.background = Image(source='background.png').texture
        return Builder.load_file('view/view.kv')

class BlackBoard(ScatterLayout):
    blocks = ObjectProperty()
    connections = ObjectProperty()
    popup = ObjectProperty(Notification())

    def execute_graph(self):
        """ Tries to execute the graph, if some block is tainted it prevents
        the execution, if not it starts running the backend. """
        logger.debug('Checking taint')
        # Check if any block is tainted
        if any(map(lambda block: block.tainted, self.blocks.children)):
            # Get tainted block
            tainted_block = reduce(lambda l, r: l if l.tainted else r,
                                   self.blocks.children)
            logger.debug('Some block is tainted')
            self.popup.title = 'Warning'
            self.popup.message = tainted_block.tainted_msg
            self.popup.open()
        else:
            logger.debug('No block is tainted')
            for block in self.blocks.children:
                if block.kindled:
                    block.unkindle()
            backend.execute_graph(self.to_ir(), self)

    def get_relations(self) -> str:
        """ Gets the relations between pins as a string. """
        # generator expressions are cool
        ins = ('{} -> {}\n'.format(block.title, in_pin.origin.end.block.title)
               for block in self.blocks.children
               for in_pin in block.input_pins if in_pin.origin)
        outs = ('{} <- {}\n'.format(block.title, destination.start.block.title)
                for block in self.blocks.children
                for out_pin in block.output_pins
                for destination in out_pin.destinations)

        return ''.join(chain(ins, outs))

    def to_ir(self) -> backend.IR:
        """ Transforms the relations between blocks into an intermediate
            representation in O(n), n being the number of pins. """
        ir_blocks = {}
        ir_inputs = {}
        ir_outputs = {}
        logger.debug('Transforming to IR')
        for block in self.blocks.children:
            if block.is_orphan():  # Ignore orphaned blocks
                continue
            block_hash = id(block)
            block_inputs, block_outputs = [], []
            avoid = False
            for in_pin in block.input_pins:
                pin_hash = id(in_pin)
                block_inputs.append(pin_hash)
                other = id(in_pin.origin.end)  # Always origin
                ir_inputs[pin_hash] = backend.InputEntry(origin=other,
                                                         pin=in_pin,
                                                         block=block_hash)
            for out_pin in block.output_pins:
                pin_hash = id(out_pin)
                block_outputs.append(pin_hash)
                dest = list(map(id, out_pin.destinations))
                ir_outputs[pin_hash] = backend.OutputEntry(destinations=dest,
                                                           pin=out_pin,
                                                           block=block_hash)
            ir_blocks[block_hash] = backend.BlockEntry(inputs=block_inputs,
                                                       function=block.function,
                                                       outputs=block_outputs)
        self.block_hashes = ir_blocks
        return backend.IR(blocks=ir_blocks, inputs=ir_inputs, outputs=ir_outputs)

    #@mainthread Concurrency bug?
    def on_block_executed(self, block_hash: int):
        """ Callback that kindles a block, pulses future connections and
        stops the pulse of past connections. """
        block_idx = list(map(id, self.blocks.children)).index(block_hash)
        block = self.blocks.children[block_idx]
        block.kindle()
        logger.debug('Kindling block {}'.format(block.__class__.__name__))

        # Python list comprehensions can be nested forwards, but also backwards
        # http://rhodesmill.org/brandon/2009/nested-comprehensions/
        [connection.pulse() for out_pin in block.output_pins
                            for connection in out_pin.destinations]
        [in_pin.origin.stop_pulse() for in_pin in block.input_pins]

    # Touch events override
    def on_touch_move(self, touch):
        if touch.button == 'left' and 'cur_line' in touch.ud.keys():
            #print(self.get_root_window().mouse_pos)
            touch.ud['cur_line'].follow_cursor(touch.pos, self)
            return True
        else:
            return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        """ Inherited from
        https://github.com/kivy/kivy/blob/master/kivy/uix/scatter.py#L590. """
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

        # if no connection was made
        if 'cur_line' in touch.ud.keys() and touch.button == 'left':
            logger.info('Connection was not finished')
            touch.ud['cur_line'].delete_connection()
            return True

        # stop propagating if its within our bounds
        if self.collide_point(x, y):
            return True

    def in_block(self, x: float, y: float) -> Optional[Block]:
        """ Check if a position hits a block. """
        for block in self.blocks.children:
            if block.collide_point(x, y):
                return block
        return None

    def spawnprint(self):
        """ Spawns a print block only if no print block is currently present.
        """
        if any(map(lambda b: b.__class__ == blocks.PrintBlock,
                       self.blocks.children)):
            self.popup.title = 'Warning'
            self.popup.message = 'Only one print block allowed!'
            self.popup.open()
        else:
            self.blocks.add_widget(blocks.PrintBlock(pos=(300, 250)))

if __name__ == '__main__':
    ViewApp().run()
