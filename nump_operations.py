import numpy as np

a = np.array([[1,0,0],[1,1,1],[2,0,0]])
b = np.array([[1,1,1],[1,1,2],[1,1,2]])

print(a+b)
print("-----")

print(a-b)
print("-----")

print(a*b)
print("-----")

print(a/b)
print("-----")

print(np.max(a))
print("-----")

print(np.min(a))
print("-----")

print(np.average(a))
print("-----")