import numpy as np

'''
Function: mixColumns(state)
Parameters: @state: 4x4 array
Description: Each column of the array will be multiplied
by the 4x4 array (finite field arithmetic):
    02 03 01 01
    01 02 03 01
    01 01 02 03
    03 01 01 02
'''

def mixColumns(state):
    
    state_o = np.zeros((4,4), dtype=np.int)

    for c in range(0,4):
        state_o[0][c] = ffMult(0x02, state[0][c]) ^ ffMult(0x03, state[1][c]) ^ state[2][c] ^ state[3][c]  
        state_o[1][c] = state[0][c] ^ ffMult(0x02, state[1][c]) ^ ffMult(0x03, state[2][c]) ^ state[3][c]
        state_o[2][c] = state[0][c] ^ state[1][c] ^ ffMult(0x02, state[2][c]) ^ ffMult(0x03, state[3][c])
        state_o[3][c] = ffMult(0x03, state[0][c]) ^ state[1][c] ^ state[2][c] ^ ffMult(0x02, state[3][c])

    return state_o

'''
Function: ffMult(a,b)
Parameters: @a -> operand 1 of multiplication
            @b -> operand 2 of multiplication
Description: Performs the multiplication for
finite fields elements (Modified peasant's 
algorithm is used)
Product is always p + a*b. Initially, the product
is a*b. After a or b is zero, product is p
'''


def ffMult(a, b):

    p = 0       #Initial value of p is 0
    
    while (a and b):                #Repeats until a or b is zero
        if (b & 0x01):              #If LSB of b is 1, adds a to p
            p ^= a                  #Finite field addition is a XOR

        if(a & 0x80):               #if a >= 128, when shifted, will overflow, so we must reduce a.
            a = (a << 1) ^0x11b     #XOR with irreducible value for XAEs (0x11b)
        else:
            a <<= 1                 #Note that left shift is equivalent to multiply by 2
        
        b >>= 1                     #Right shift B to analyse next bit in next iteration

    return p

   
