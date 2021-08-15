# Dependencies
from functools import reduce

# The data
s = {1,2,3}

# The One-liner
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

# The result
print(ps(s))