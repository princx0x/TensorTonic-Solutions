from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    dict = {}
    val = {}
    lst = sorted(x)
    if len(lst)%2==1:
        dict["median"] = float(lst[len(lst)//2])
    else:
        dict["median"] = (lst[len(lst)//2 -1] + lst[len(lst)//2])/2
    dict["mean"] = sum(x)/len(x)
    z = []
    for i in set(x):
        val[i] = x.count(i)
    for i in val.keys():
        if val[i] == max(val.values()):
            z.append(i)

    dict["mode"] = float(min(z))

    return dict
    
    