import numpy as np

'''
Function: shiftRows(state)
Parameters: @state. A 4x4 array
Description: Shifts each row of matrix
    First line  -> 0 1 2 3
    Second line -> 1 2 3 0
    Third line  -> 2 3 0 1
    Fourth lune -> 3 0 1 2
'''


def shiftRows(state):
    
    aux = []    #Aux list
    
    for i, row in zip(range(0,4),state):
        aux.append(np.roll(row, -i, axis=0))    #shifts each row

    return np.array(aux)    #Returns shifted Array
