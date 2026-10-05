import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    eig_values = np.linalg.eigvals(matrix)
    eig_values.sort()
    return np.array(eig_values)