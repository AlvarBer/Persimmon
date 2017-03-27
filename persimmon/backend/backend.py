import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split, KFold


def perform(train_data, estimator, cv, predict_data=np.array(0)):
    X, y = train_data.iloc[:, :-1], train_data.iloc[:, -1]
    if not predict_data.shape:
        return cross_val_score(estimator, X, y, cv=cv)
    else:
        return estimator.fit(X, y).predict(predict_data)

"""
def execute_graph():
    queue = deque()
    seen = {}
    queue.append(self.blocks[0])
    while queue:
        queque, seen = self.explore_graph(queue.popleft(), queue, seen)

def explore_graph(graph, block, queue: deque, seen: dict) -> (deque, dict):
    args = []
    for in_pin in graph[block].inputs:
        if in_pin not in seen:
            dependency = in_pin
            if dependency in queue:
                queue.remove(dependency)
            queue, seen = self.explore_graph(dependency, queue, seen)
        args.append(seen[pin_uid])
    result = graph[block].function(*args)
    for out_pin in graph[block].outputs:
        seen[out_pin] = result[i]
        for future_block in map(lambda x: x.block, out_pin.destinations):
            if future_block not in queue:
                queue.append(future_block)

    return queue, seen
"""

if __name__ == '__main__':
    est = SVC()
    df = pd.read_csv('~/Downloads/iris.csv', header=0)
    print(perform(df, est, None, df.iloc[:, :-1]))

