# Deopendencies
import numpy as np

# Stock Price Data: 5 companies
# (row=[price_day_1, price_2, ..., price_day_n])
x = np.array([[8,9,11,12],
              [1,2,2,1],
              [2,8,9,9],
              [9,6,6,3],
              [3,3,3,3]])

# One-liner
avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

# Result & puzzle
print("Averages: " + str(avg))
print("Variance: " + str(var))
print("Standard Deviations: " + str(std))