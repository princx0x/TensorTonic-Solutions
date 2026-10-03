import numpy as np

def sample_var_std(x: list) -> dict:
    mean = sum(x)/len(x)

    var = 0
    for i in range(len(x)):
        var += (x[i]-mean)**2
    variance = var/(len(x)-1)
    std = np.sqrt(variance)

    return {"variance":float(variance), "standard_deviation":float(std)}