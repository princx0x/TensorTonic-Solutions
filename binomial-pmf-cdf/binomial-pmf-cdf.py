import math
def combination(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

    
def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    pmf = combination(n,k)*((p)**k)*((1-p)**(n-k))
    cdf = 0
    for i in range(k+1):
        cdf+=combination(n,i)*((p)**i)*((1-p)**(n-i))


    return {"pmf":float(pmf),"cdf":float(cdf)}