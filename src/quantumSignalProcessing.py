import numpy as np
import exceptions as ex
 
def signalRotationOp(a): 
    '''
    For an input a = [-1, 1] this function computates the z rotation in the bloch sphere
    by an angle theta = -2 * arccos(a). 
    The matrix is given by:
               __                                      __                                
              | a                      i * sqrt(1 - a^2) |
     W [s] =  |                                          |           
              | i * sqrt(1 - a^2)      a                 |
              |__                                      __| 
    '''
    ex.SRO(a)
    sqrt = np.sqrt(1-np.square(a))
    matrix = np.array([[a, 1j*sqrt], [1j*sqrt, a]])
    return matrix

def signalProcessingRotationOp(phi): 
    '''
    With the input phi, this function computes the z rotation in the bloch sphere 
    by an angle theta = -2 * phi.
    The matrix is given by:
                 __                                      __
                | exp(i * phi)               0             |
     S [phi] =  |                                          | = exp(i * phi * Z)
                | 0                          exp(-i * phi) |
                |__                                      __|
    '''
    ex.SPRO(phi)
    matrix = np.array([[np.exp(1j * phi), 0], [0, np.exp(1j * -phi)]])
    return matrix

def quantumSignalProcessing(phi_vec, a):
    '''
    Transforms a scalar value `a` into a polynomial function using unitary operations.
    
    Parameters:
        phi_vec (list): List of angles (phi) used in the unitary transformation.
        a (float): Scalar value (must satisfy |a| <= 1 for the sqrt(1 - a^2) to be valid).
    
    Returns:
        numpy.ndarray: The resulting matrix representing the polynomial function.

    The matrix has the form:
                  __                                                  __
                 | P(a)                        i * Q(a) * sqrt(1 - a^2) |
    U_phi_vec =  |                                                      | 
                 | i * Q_d(a) * sqrt(1 - a^2)  P_d(a)                   |  
                 |__                                                  __|
    '''
    SRO = signalRotationOp(a)
    res = signalProcessingRotationOp(phi_vec[0])
    for i in range(1, len(phi_vec)):
        res = res @ SRO @ signalProcessingRotationOp(phi_vec[i])
    return res
