import numpy as np
from scipy.linalg import eigvals

def blockEncoding(A):
   # matrix = np.array([[0, A], [A, 0]])
    U = np.kron(np.array([[1, 0], [0, -1]]), A) + np.kron(np.array([[0, 1], [1, 0]]), sqrtm(np.eye(A.shape[0]) - A @ A))
    assert np.allclose(U @ U.conj().T, np.eye(2 * len(A)), atol=1e-5), "For this block-encoding to work, A must be square and its spectral norm must be <= 1."
    return U

def projectorControlledPhaseShift(phi, proj):
    #projector 	 := |0> <0| 
    return np.exp(1j * 2 * phi * proj)

def quantumEigenvalueTransform(U, phi_vec):
    P = np.kron(np.array([[1, 0], [0, 0]]), np.eye(len(U) // 2))

    res = projectorControlledPhaseShift(P, phi_vec[0])
    for i in range(1, len(phi_vec)):
        res = res @ U @ projectorControlledPhaseShift(P, phi_vec[i])

    return res 
