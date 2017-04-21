from collections import deque, namedtuple


# backend types
InputEntry = namedtuple('InputEntry', ['origin', 'pin', 'block'])
BlockEntry = namedtuple('BlockEntry', ['inputs', 'function', 'outputs'])
OutputEntry = namedtuple('OutputEntry', ['destinations', 'pin', 'block'])
IR = namedtuple('IR', ['blocks', 'inputs', 'outputs'])

def execute_graph(ir: IR):
    queue = deque()
    seen = {}  # Saves seen output pins and blocks
    unexplored = set(ir.blocks.keys())
    while unexplored:
        unexplored, seen = explore_graph(unexplored.pop(), ir, unexplored, seen) 

def explore_graph(current: int, ir: IR, unexplored: set, seen: {int: OutputEntry}) -> (deque, {int: OutputEntry}):
    #print('executing block {}'.format(current))
    current_block = ir.blocks[current]
    for in_pin in map(lambda x: ir.inputs[x], current_block.inputs):
        origin = in_pin.origin
        if origin not in seen:
            dependency = ir.outputs[origin].block
            unexplored.remove(dependency)
            unexplored, seen = explore_graph(dependency, ir, unexplored, seen)
        in_pin.pin.val = seen[origin]

    current_block.function()

    for out_id in current_block.outputs:
        seen[out_id] = ir.outputs[out_id].pin.val
    #print('Done executing {}'.format(current))
    return unexplored, seen

