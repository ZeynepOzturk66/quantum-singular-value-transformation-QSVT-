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

