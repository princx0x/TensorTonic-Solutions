import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    res = 0
    for i in range(len(y_true)):
        res += (y_true[i] - y_pred[i])**(2)

    res /= len(y_true)

    return res