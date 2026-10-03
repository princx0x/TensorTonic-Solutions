import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    var = 0
    for i in range(len(x)):
        var += x[i]*p[i]

    return float(var)