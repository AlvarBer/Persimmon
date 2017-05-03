from collections import deque, namedtuple
import threading
import logging


logger = logging.getLogger(__name__)

# backend types
InputEntry = namedtuple('InputEntry', ['origin', 'pin', 'block'])
BlockEntry = namedtuple('BlockEntry', ['inputs', 'function', 'outputs'])
OutputEntry = namedtuple('OutputEntry', ['destinations', 'pin', 'block'])
IR = namedtuple('IR', ['blocks', 'inputs', 'outputs'])

def execute_graph(ir: IR, blackboard):
    threading.Thread(target=execute_graph_parallel,
                     args=(ir, blackboard)).start()
    logger.info('Execution done')

def execute_graph_parallel(ir: IR, blackboard):
    """ Execution algorithm, introduces all blocks on a set, when a block is
    executed it is taken out of the set until the set is empty. """
    unexplored = set(ir.blocks.keys())  # All blocks are unexplored at start
    seen = {}  # All output pins along their respectives values
    while unexplored:
        unexplored, seen = execute_block(unexplored.pop(), ir, blackboard,
                                         unexplored, seen)

def execute_block(current: int, ir: IR, blackboard, unexplored: set, seen: {}) -> (set, {}):
    """ Execute a block, if any dependency is not yet executed we
    recurse into it first. """
    logger.debug('executing block {}'.format(current))
    current_block = ir.blocks[current]
    for in_pin in map(lambda x: ir.inputs[x], current_block.inputs):
        origin = in_pin.origin
        if origin not in seen:
            dependency = ir.outputs[origin].block
            unexplored.remove(dependency)
            unexplored, seen = execute_block(dependency, ir, blackboard, unexplored, seen)
        in_pin.pin.val = seen[origin]

    current_block.function()
    blackboard.on_block_executed(current)
    logger.debug('block {} executed'.format(current))

    for out_id in current_block.outputs:
        seen[out_id] = ir.outputs[out_id].pin.val
    return unexplored, seen

