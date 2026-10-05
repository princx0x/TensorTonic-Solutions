import numpy as np

def std(x: list) -> dict:
    mean = sum(x)/len(x)

    var = 0
    for i in range(len(x)):
        var += (x[i]-mean)**2
    variance = var/(len(x)-1)
    std = variance**0.5
    return std
    
def t_test_one_sample(x: list, mu0: float) -> float:
    mean = sum(x)/len(x)
    s = std(x)
    if s == 0 and mean == mu0:
        return 0.0
    elif s== 0 and mean != mu0:
        return float("inf")
    else:
        t = (mean - mu0)/s
        t*= len(x)**0.5

        return float(t)