# The Data
n = 20

# The one-liner
factorial = lambda n: n*factorial(n-1) if n>1 else 1

# The result
print(factorial(n))