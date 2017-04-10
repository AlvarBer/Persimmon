import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from collections import deque, namedtuple
from typing import TypeVar


# backend types
T = TypeVar('T')
InputEntry = namedtuple('InputEntry', ['origin', 'pin', 'block'])
BlockEntry = namedtuple('BlockEntry', ['inputs', 'function', 'outputs'])
OutputEntry = namedtuple('OutputEntry', ['destinations', 'pin', 'block'])
IR = namedtuple('IR', ['blocks', 'inputs', 'outputs'])

def execute_graph(ir: IR):
    queue = deque()
    seen = {}
    queue.append(list(ir.blocks.keys())[0])  # Random start
    while queue:
        queque, seen = explore_graph(queue.popleft(), ir, queue, seen)
    print('Execution done!')

def explore_graph(current: int, ir: IR, queue: deque, seen: {int: T}) -> (deque, {int: T}):
    current_block = ir.blocks[current]
    for in_pin in map(lambda x: ir.inputs[x], current_block.inputs):
        origin = in_pin.origin
        if origin:
            if origin not in seen:
                dependency = ir.outputs[origin].block
                if dependency in queue:
                    queue.remove(dependency)
                queue, seen = explore_graph(dependency, ir, queue, seen)
            in_pin.pin.val = seen[origin]
    current_block.function()
    for out_id in current_block.outputs:
        seen[out_id] = ir.outputs[out_id].pin.val
        for future_block in [ir.inputs[x].block for x in ir.outputs[out_id].destinations]:
            if future_block not in queue:
                queue.append(future_block)
    return queue, seen


if __name__ == '__main__':
    est = SVC()
    df = pd.read_csv('~/Downloads/iris.csv', header=0)
    print(perform(df, est, None, df.iloc[:, :-1]))

