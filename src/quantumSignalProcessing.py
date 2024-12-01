import numpy as np
import exceptions as ex

def signalRotationOp(a): 
    #for a value a = [-1, 1]
    ex.SRO(a)
    sqrt = np.sqrt(1-np.square(a))
    matrix = np.array([[a, 1j*sqrt], [1j*sqrt, a]])
    return matrix

def signalProcessingRotationOp(phi): 
    # for a value phi = [0, 2pi]
    ex.SPRO(phi)
    matrix =  np.array([[np.exp(1j * phi), 0], [0, np.exp(1j * -phi)]])
    return matrix

def quantumSignalProcessing(phi_vec, a):
    w = signalRotationOp(a)
    res = signalProcessingRotationOp(phi_vec[0])
    for i in range(1, len(phi_vec)):
        res = res @ w @ signalProcessingRotationOp(phi_vec[i])
    # @ -> Matrixmultiplication    
    print("Quantum signal processing: \n", res)    
    return res
