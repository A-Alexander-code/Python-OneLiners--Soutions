import numpy as np

a = np.array([1, -1, 2, -2])
print(a)
print(np.abs(a))

b = np.array([True, True, True, False])
c = np.array([False, True, True, False])

print(np.logical_and(b,c))