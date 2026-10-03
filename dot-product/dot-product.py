import numpy as np

def dot_product(x: list, y: list) -> float:
    sum_var = 0
    for i in range(len(x)):
        sum_var += x[i]*y[i]

    return float(sum_var)
        
