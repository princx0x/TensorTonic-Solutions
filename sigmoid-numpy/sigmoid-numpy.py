import numpy as np

def fn(x):
    return 1/(1+np.exp(-1*x))
def sigmoid(x: list | float) -> np.ndarray | float:
    array = np.array(x)

    return fn(array)
        