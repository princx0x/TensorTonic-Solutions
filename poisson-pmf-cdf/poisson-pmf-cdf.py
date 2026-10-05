import math
import numpy as np

def prob(lam,k):
    res = ((math.e)**(-1*lam) )*(lam**k)
    res = res/math.factorial(k)

    return res

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    pmf = prob(lam,k)

    cdf = 0
    for i in range(k+1):
        cdf+=prob(lam,i)

    return {"pmf":pmf,"cdf":cdf}