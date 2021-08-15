def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(prime(10))
print(prime(11))
print(prime(7919))

# Find all prime numbers <= m
m = 20
primes = [n for n in range(2, m+1) if prime(n)]

print(primes)