import numpy as np

def quantumEigenvalueTransform(A, t):
    return np.linalg.matrix_power(A, t)
