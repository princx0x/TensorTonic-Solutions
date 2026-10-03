import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    out = []
    try:
        for i in range(len(A[0])):
            out.append([])
        #print(out)
        
        for j in range(len(A)):#2
            for k in range(len(A[0])):
                    out[k].append(A[j][k])

        return np.array(out)
    except:
        return np.array([])