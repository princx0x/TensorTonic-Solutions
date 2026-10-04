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
    
        