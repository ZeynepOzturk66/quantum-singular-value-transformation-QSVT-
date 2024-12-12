import numpy as np
import exceptions as ex
from scipy.linalg import sqrtm
from scipy.linalg import expm

def blockEncoding(A: np.ndarray):
    '''
    Constructs the block-encoding matrix U for a given matrix A.

    Parameters:
        A (numpy.ndarray): A square matrix satisfying ||A|| <= 1, 
                           where ||A|| is the spectral norm of A.

    Returns:
        numpy.ndarray: The block-encoding matrix U.

    Raises:
        AssertionError: If A is not square or its spectral norm is greater than 1.
    '''
    ex.BEC(A)

    Z = np.array([[1, 0], [0, -1]]) # Pauli-Z matrix
    X = np.array([[0, 1], [1, 0]])  # Pauli-X matrix
    I = np.eye(A.shape[0])          # Identity matrix

    U = np.kron(Z, A) + np.kron(X, sqrtm(I - A @ A))
    assert np.allclose(U @ U.conj().T, np.eye(2 * A.shape[0]), atol=1e-5), \
        "The block encoding matrix U is not unitary. Check matrix A."
    return U

def projectorControlledPhaseShift(phi: float, proj: np.ndarray):
    '''
    Implements the projector-controlled phase-shift operation.

    Parameters:
        phi (float): The phase shift angle in radians.
        proj (numpy.ndarray): The projector matrix (must satisfy proj^2 = proj).
    
    Returns:
        numpy.ndarray: The resulting unitary matrix representing the operation.
    '''
    ex.PCPS(phi, proj)
    I = np.eye(proj.shape[0])       
    U = expm(1j * phi * (2 * proj - I))
    return U

def quantumEigenvalueTransform(A: np.ndarray, phi_vec: list):
    '''
    Applies a quantum eigenvalue transformation on a given matrix A by first constructing
    its block encoding and then applying the transformation.

    Parameters:
        A (numpy.ndarray): The input square matrix satisfying ||A|| <= 1.
        phi_vec (list of float): A list of phase angles defining the transformation.

    Returns:
        numpy.ndarray: The resulting matrix after applying the quantum eigenvalue transformation.
    '''
    ex.QEV(phi_vec, A)
    U = blockEncoding(A)
    P = np.kron(np.array([[1, 0], [0, 0]]), np.eye(len(U) // 2))
    res = projectorControlledPhaseShift(phi_vec[0], P)
    for i in range(1, len(phi_vec)):
        res = res @ U @ projectorControlledPhaseShift(phi_vec[i], P)
    return res

