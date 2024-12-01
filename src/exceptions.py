import numpy as np

def exceptions(): 
    return 0

def SRO(a): 
    if a < -1 or a > 1:
        raise ValueError("The value of a must be between -1 and 1.")
    #falls wert zu klein ist
    #Grenzen meines Programms

def SPRO(phi): 
    if phi < 0 or phi > 2 * np.pi:
        raise ValueError("The value of phi must be between 0 and 2pi.")
    
