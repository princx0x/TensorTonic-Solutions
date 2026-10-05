import numpy as np
def covariance_matrix(X: list) -> np.ndarray:
    Xc = []
    Mu = [0 for i in range(len(X[0]))]
    for i in X:
        for j in range(len(X[0])):
            Mu[j]+= i[j]

    Mu = np.array([i/len(X) for i in Mu])

    for k in X:
        Xc.append(np.array(k) - Mu) 

    output = np.transpose(np.array(Xc))@np.array(Xc)

    return output/(len(X) - 1)


def std(x: list) -> float:
    mean = sum(x)/len(x)
    var = 0
    for i in range(len(x)):
        var += (x[i]-mean)**2
    variance = var/(len(x)-1)
    std = np.sqrt(variance)
    return std;

def pearson_correlation(X: list) -> np.ndarray:
    cov = covariance_matrix(X)

    feature = []
    for i in range(len(X[0])):
        feature.append([])
        for j in range(len(X)):
            feature[i].append(X[j][i])
    val = []

    
    for i in feature:
        val.append(std(i))

    for i in range(len(cov)):
        for j in range(len(cov[0])):
            cov[i][j] = cov[i][j]/(val[i]*val[j])

    return np.array(cov)

    