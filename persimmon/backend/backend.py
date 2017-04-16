import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from collections import deque, namedtuple
from enum import Enum, auto


class Test(Enum):
    NIL = auto()

# backend types
InputEntry = namedtuple('InputEntry', ['origin', 'pin', 'block'])
BlockEntry = namedtuple('BlockEntry', ['inputs', 'function', 'outputs'])
OutputEntry = namedtuple('OutputEntry', ['destinations', 'pin', 'block'])
IR = namedtuple('IR', ['blocks', 'inputs', 'outputs'])

def execute_graph(ir: IR):
    queue = deque()
    seen = {}  # Saves seen output pins and blocks
    for block in ir.blocks:
        if block not in seen:
            queue.append(block)
            while queue:
                queque, seen = explore_graph(queue.popleft(), ir, queue, seen)
    print('Execution done!')

def explore_graph(current: int, ir: IR, queue: deque, seen: {int: OutputEntry}) -> (deque, {int: OutputEntry}):
    #print('Executing block {}'.format(current))
    current_block = ir.blocks[current]
    for in_pin in map(lambda x: ir.inputs[x], current_block.inputs):
        origin = in_pin.origin
        if origin:
            if origin not in seen:
                dependency = ir.outputs[origin].block
                if dependency in queue:
                    queue.remove(dependency)
                queue, seen = explore_graph(dependency, ir, queue, seen)
            if seen[origin] is not Test.NIL:
                in_pin.pin.val = seen[origin]
                continue
        seen[current] = None
        seen = taint_block(current_block, seen)
        return queue, seen

    current_block.function()
    seen[current] = Test.NIL

    for out_id in current_block.outputs:
        seen[out_id] = ir.outputs[out_id].pin.val
        for future_block in [ir.inputs[x].block for x in ir.outputs[out_id].destinations]:
            if future_block not in queue:
                queue.append(future_block)
    return queue, seen

def taint_block(block, seen):
    for out_id in block.outputs:
        seen[out_id] = Test.NIL  # Tainted
    return seen

