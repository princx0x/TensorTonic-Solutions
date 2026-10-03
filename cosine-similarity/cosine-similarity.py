import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    dot = 0
    ea = 0
    eb = 0
    
    for i in range(len(a)):
        dot+= a[i]*b[i]
        ea+= a[i]**2
        eb += b[i]**2
    
    ea = np.sqrt(ea)
    eb = np.sqrt(eb)
    if ea == 0 or eb == 0:
        return float(0)
    else:
        return float(dot/(ea*eb))

    