import numpy as np
import math

def l1(x : list):
    out = 0
    for i in x:
        out+= abs(i)
        
    return out

def l2(x : list):
    out = 0
    for i in x:
        out += i**2
    return out**(0.5)

def lmax(x : list):
    out = []
    for i in x:
        out.append(abs(i))
    return max(out)


def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    out = []
    if norm_type == "l1":
        if axis == 1:
            for i in matrix:
                out.append(np.array(i)/ l1(i))
        elif axis == 0:
            matrix = np.transpose(matrix)
            for i in matrix:
                out.append(np.array(i)/ l1(i))
            out = np.transpose(np.array(out))
            
        else:
            lst = []
            for i in matrix:
                lst += i
            out = np.array(matrix)/l1(lst)
    elif norm_type == "l2":
        if axis == 1:
            for i in matrix:
                out.append(np.array(i)/ l2(i))
        elif axis == 0:
            matrix = np.transpose(matrix)
            for i in matrix:
                out.append(np.array(i)/ l2(i))
            out = np.transpose(np.array(out))
            
        else:
            lst = []
            for i in matrix:
                lst += i
            out = np.array(matrix)/l2(lst)
    elif norm_type == "max":
        if axis == 1:
            for i in matrix:
                out.append(np.array(i)/ lmax(i))
        elif axis == 0:
            matrix = np.transpose(matrix)
            for i in matrix:
                out.append(np.array(i)/ lmax(i))
            out = np.transpose(np.array(out))
            
        else:
            lst = []
            for i in matrix:
                lst += i
            out = np.array(matrix)/lmax(lst)


    for i in range(len(out)):
        for j in range(len(out[0])):
            if math.isnan(out[i][j]):
                out[i][j] = 0 
            
    return np.array(out)