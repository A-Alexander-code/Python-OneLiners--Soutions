# Dependencies
import numpy as np

# Data (rows: stocks/ cols: stock prices)
x = np.array([[25,27,29,30],
              [1,5,3,2],
              [12,11,8,3],
              [1,1,2,2],
              [2,6,2,2]])

# One-liner
# Find the stock with the smallest variance
min_row = min([(i,np.var(x[i,:])) for i in range(len(x))], key=lambda x : x[1])

# Result & puzzle
print("Row with minimun variance: " + str(min_row[0]))
print("Variance: " + str(min_row[1]))

# Another solution
var = np.var(x, axis=1)
min_row = (np.where(var==min(var)).min(var))