# The data
unsorted = [33, 2, 3, 45, 6, 54, 33]

# The one-liner
q = lambda l: q([x for x in l[1:] if x<=l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

# The result
print(q(unsorted))