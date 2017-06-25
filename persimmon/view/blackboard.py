# We need blocks to make a few checks
from persimmon.view import blocks
from persimmon.view.util import Notification
from persimmon import backend
from persimmon.backend import IR  # For type checking only
# Kivy classes for inheritance
from kivy.uix.widget import Widget
from kivy.uix.scatterlayout import ScatterLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# Just for type hinting
from kivy.input import MotionEvent
from functools import reduce
from itertools import chain
import logging
from typing import Optional


Builder.load_file('persimmon/view/blackboard.kv')
logger = logging.getLogger(__name__)

class BlackBoard(ScatterLayout):
    """ Widget containing blocks and connections, it can be moved and zoomed
    (sometime on the future). """
    block_div = ObjectProperty()  # Block child reference
    connections = ObjectProperty()  # Connection child reference

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.backend = backend.Backend()
        self.backend.on('block_executed', self.on_block_executed)
        self.backend.on('graph_executed', self.on_graph_executed)

    def execute_graph(self):
        """ Tries to execute the graph, if some block is tainted it prevents
        the execution, if not it starts running the backend. """
        logger.debug('Checking taint')
        # Check if any block is tainted
        if any(map(lambda block: block.tainted, self.block_div.children)):
            # Get tainted block
            tainted_block = reduce(lambda l, r: l if l.tainted else r,
                                   self.block_div.children)
            logger.debug('Some block is tainted')
            Notification(title='Warning',
                         message=tainted_block.tainted_msg).open()
            self.parent.on_graph_executed()
        else:
            logger.debug('No block is tainted')
            for block in self.block_div.children:
                if block.kindled:
                    block.unkindle()
            self.backend.exec_graph(self.to_ir())

    def get_relations(self) -> str:
        """ Gets the relations between pins as a string. """
        # generator expressions are cool
        ins = ('{} -> {}\n'.format(block.title, in_pin.origin.end.block.title)
               for block in self.block_div.children
               for in_pin in block.input_pins if in_pin.origin)
        outs = ('{} <- {}\n'.format(block.title, destination.start.block.title)
                for block in self.block_div.children
                for out_pin in block.output_pins
                for destination in out_pin.destinations)

        return ''.join(chain(ins, outs))

    def to_ir(self) -> IR:
        """ Transforms the relations between blocks into an intermediate
            representation in O(n), n being the number of pins. """
        ir_blocks = {}
        ir_inputs = {}
        ir_outputs = {}
        logger.debug('Transforming to IR')
        for block in self.block_div.children:
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

    #@mainthread
    def on_block_executed(self, block_hash: int):
        """ Callback that kindles a block, pulses future connections and
        stops the pulse of past connections. """
        block_idx = list(map(id, self.block_div.children)).index(block_hash)
        block = self.block_div.children[block_idx]
        block.kindle()
        logger.debug('Kindling block {}'.format(block.__class__.__name__))

        # Python list comprehensions can be nested forwards, but also backwards
        # http://rhodesmill.org/brandon/2009/nested-comprehensions/
        [connection.pulse() for out_pin in block.output_pins
                            for connection in out_pin.destinations]
        [in_pin.origin.stop_pulse() for in_pin in block.input_pins]

    def on_graph_executed(self):
        # TODO: Fix this
        self.parent.on_graph_executed()

    # Touch events override
    def on_touch_down(self, touch: MotionEvent) -> bool:
        if self.collide_point(*touch.pos):  # There is a current bubble
            if not super().on_touch_down(touch) and touch.button == 'right':
                self.add_widget(blocks.SmartBubble(pos=touch.pos, backdrop=self))
                return True
            else:
                return False
        else:
            return False

    def on_touch_move(self, touch: MotionEvent) -> bool:
        if touch.button == 'left' and 'cur_line' in touch.ud.keys():
            #print(self.get_root_window().mouse_pos)
            touch.ud['cur_line'].follow_cursor(touch.pos, self)
            return True
        else:
            return super().on_touch_move(touch)

    def on_touch_up(self, touch: MotionEvent) -> bool:
        """ Inherited from
        https://github.com/kivy/kivy/blob/master/kivy/uix/scatter.py#L590. """
        if self.disabled:
            return False

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
            logger.info('Finish connection through smart bubble')
            connection = touch.ud['cur_line']
            if connection.forward:
                edge = connection.start
            else:
                edge = connection.end
            self.add_widget(blocks.SmartBubble(pos=touch.pos, backdrop=self, pin=edge))
            return True

        # stop propagating if its within our bounds
        if self.collide_point(x, y):
            return True
        return False

    def in_block(self, x: float, y: float) -> Optional[blocks.Block]:
        """ Check if a position hits a block. """
        for block in self.block_div.children:
            if block.collide_point(x, y):
                return block
        return None


class Blocks(Widget):
    """ Blocks is a vanilla widget that contains all blocks, it overrides add
    and remove widget methods for showing/hiding the hint. """
    def add_widget(self, widget: Widget, index: int = 0, canvas: str = None):
        """ Add widget override. """
        if (widget.__class__ == blocks.PrintBlock and
            any(map(lambda w: w.__class__ == blocks.PrintBlock, self.children))):
            Notification(title='Warning',
                         message='Only one print block allowed!').open()
            return
        if not self.children:
            self.parent.parent.parent.remove_hint()
        super().add_widget(widget, index, canvas)

    def remove_widget(self, widget: Widget):
        """ Remove widget override. """
        super().remove_widget(widget)
        if not self.children:
            self.parent.parent.parent.add_hint()

