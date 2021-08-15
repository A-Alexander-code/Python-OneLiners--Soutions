n = 10

x = [0,1]

fibs = x[0:2] + [x.append(x[-1] + x[-2]) or x[-1] for i in range (n-2)]

print(fibs)