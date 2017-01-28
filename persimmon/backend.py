
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split, KFold

def perform(train_data, estimator, cv, predict_data=None):
    X, y = train_data.iloc[:, :-1], train_data.iloc[:, -1]
    if not predict_data:
        return cross_val_score(estimator, X, y, cv=cv)
    else:
        return estimator.fit(X, y).predict(predict_data)


if __name__ == '__main__':
    est = SVC()
    df = pd.read_csv('~/Downloads/iris.csv', header=0)
    cv = KFold()
    print(perform(df, est, None))

