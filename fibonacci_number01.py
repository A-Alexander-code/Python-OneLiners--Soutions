# Dependencies
from functools import reduce

# The data
n = 10

# The one-liner
fibs = reduce(lambda x,_: x+[x[-2]+x[-1]], [0]*(n-2), [0,1])

# The result
print(fibs)