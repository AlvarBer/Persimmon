from threading import Thread
from pymitter import EventEmitter
from typing import List, Dict, Any, Tuple, NamedTuple, Callable, TYPE_CHECKING
from persimmon.view.pins import Pin  # For typing only
import logging


logger = logging.getLogger(__name__)

# backend types
InputEntry = NamedTuple('InputEntry', [('origin', int),
                                       ('pin', 'Pin'),
                                       ('block', int)])
BlockEntry = NamedTuple('BlockEntry', [('inputs', List[int]),
                                       ('function', Callable[..., None]),
                                       ('outputs', List[int])])
OutputEntry = NamedTuple('OutputEntry', [('destinations', List[int]),
                                         ('pin', 'Pin'),
                                         ('block', int)])
IR = NamedTuple('IR', [('blocks', Dict[int, BlockEntry]),
                       ('inputs', Dict[int, InputEntry]),
                       ('outputs', Dict[int, OutputEntry])])

class Backend(EventEmitter):
    def exec_graph(self, ir: IR):
        self.ir = ir
        Thread(target=self._exec_graph_parallel).start()

    def _exec_graph_parallel(self):
        """ Execution algorithm, introduces all blocks on a set, when a block
        is executed it is taken out of the set until the set is empty. """
        unseen = set(self.ir.blocks.keys())  # All blocks are unseen at start
        # All output pins along their respectives values
        seen = {}  # type: Dict[int, Any]
        while unseen:
            unseen, seen = self._exec_block(unseen.pop(), unseen, seen)
        logger.info('Execution done')
        self.emit('graph_executed')

    def _exec_block(self, current: int, unseen: set,
                    seen: Dict[int, Any]) -> Tuple[set, Dict[int, Any]]:
        """ Execute a block, if any dependency is not yet executed we
        recurse into it first. """
        logger.debug('Executing block {}'.format(current))
        current_block = self.ir.blocks[current]
        for in_pin in map(lambda x: self.ir.inputs[x], current_block.inputs):
            origin = in_pin.origin
            if origin not in seen:
                dependency = self.ir.outputs[origin].block
                unseen.remove(dependency)
                unseen, seen = self._exec_block(dependency, unseen, seen)
            in_pin.pin.val = seen[origin]

        current_block.function()
        self.emit('block_executed', current)
        logger.debug('Block {} executed'.format(current))

        for out_id in current_block.outputs:
            seen[out_id] = self.ir.outputs[out_id].pin.val
        return unseen, seen

