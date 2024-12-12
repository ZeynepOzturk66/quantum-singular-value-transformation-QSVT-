import numpy as np

def SRO(a): 
    '''
    Validates the input for the signal rotation operation.

    Parameters:
        a (float): Input value for the signal rotation.

    Raises:
        ValueError: If a is not between -1 and 1.
        TypeError: If a is not a number.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("The value of 'a' must be a number.")
    if a < -1 or a > 1:
        raise ValueError("The value of 'a' must be between -1 and 1.")

def SPRO(phi): 
    '''
    Validates the input for the signal processing rotation operation.

    Parameters:
        phi (float): Input angle in radians.

    Raises:
        ValueError: If phi is not between 0 and 2*pi.
    '''
    if phi < 0 or phi > 2 * np.pi:
        raise ValueError("The value of phi must be between 0 and 2*pi.")

def BEC(A): 
    '''
    Validates the input matrix for block encoding.

    Parameters:
        A (numpy.ndarray): Input matrix to validate.

    Raises:
        AssertionError: If A is not square or its spectral norm is greater than 1.
    '''
    if not A.shape[0] == A.shape[1]:
        raise AssertionError("A must be a square matrix.")
    
    if np.linalg.norm(A, ord=2) > 1: 
        raise AssertionError("The spectral norm of A must be <= 1.")
    
def PCPS(phi, proj):
    '''
    Validates the input for the phase shift operation.

    Parameters:
        phi (float): The phase shift angle in radians.
        proj (numpy.ndarray): The projector matrix (must satisfy proj^2 = proj).

    Raises:
        TypeError: If phi is not a number or proj is not a numpy array.
        ValueError: If proj is not a valid projector or proj is not square.
    '''
    if not isinstance(phi, (int, float)):
        raise TypeError("The value of `phi` must be a number.")
    if not isinstance(proj, np.ndarray):
        raise TypeError("The projector must be a numpy array.")
    if proj.shape[0] != proj.shape[1]:
        raise ValueError("The projector must be a square matrix.")
    if not np.allclose(proj @ proj, proj, atol=1e-10):
        raise ValueError("The projector does not satisfy the condition P^2 = P.")

def QEV(phi_vec, proj): 
    '''
    Validates the input for the quantum eigenvalue transformation.

    Parameters:
        phi_vec (list of float): A list of phase angles in radians.
        proj (numpy.ndarray): Input projector matrix.

    Raises:
        TypeError: If phi_vec is not a list or numpy array, or if elements in phi_vec are not numbers.
        ValueError: If proj is not a valid projector or is not square.
    '''
    if not isinstance(phi_vec, (list, np.ndarray)):
        raise TypeError("The value of `phi_vec` must be a list or numpy array.")
    if not all(isinstance(phi, (int, float)) for phi in phi_vec):
        raise TypeError("All elements in `phi_vec` must be numbers.")
    
    if not isinstance(proj, np.ndarray):
        raise TypeError("The projector must be a numpy array.")
    if proj.shape[0] != proj.shape[1]:
        raise ValueError("The projector must be a square matrix.")
    if not np.allclose(proj @ proj, proj, atol=1e-10):
        raise ValueError("The projector does not satisfy the condition P^2 = P.")
