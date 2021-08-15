# Dependencies
from functools import reduce

# The data
n = 100

# The one-liner
primes = reduce(lambda r, x: r-set(range(x**2, n, x)) if x in r else r,
                range(2, int(n**0.5)+1), set(range(2,n)))

# The result
print(primes)