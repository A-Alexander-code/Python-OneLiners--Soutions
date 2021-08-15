import numpy as np
x = np.array([[[1, 2], [1, 1]],
              [[1, 1], [2, 1]],
              [[1, 0], [0, 0]]])

print(np.average(x, axis=2))
print("-----------")
print(np.var(x, axis=2))
print("-----------")
print(np.std(x, axis=2))