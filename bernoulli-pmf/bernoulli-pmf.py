import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    lst = []
    for i in x:
        lst.append(1-p if i==0 else p)
    Res = {
        "pmf":np.array(lst),
        "mean":float(p),
        "variance":float((1-p)*p)
    }
    return Res