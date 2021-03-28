import subBytes
import numpy as np

np.set_printoptions(formatter={'int':hex})
a = np.random.randint(0, 0xff, (16,16))

print('State before:')
print(a)

state = subBytes.subBytes(a)

print('State after subBytes:')

print(state)

