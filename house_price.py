# Dependencies
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# Data (House Size ((square meters)/House price($))
x = np.array([[35, 30000], [45, 45000], [40, 50000], 
              [35, 35000], [25, 32500], [40, 40000]])

# One-liner
knn = KNeighborsRegressor(n_neighbors = 3).fit(x[:,0].reshape(-1,1), x[:,1])

# Result & puzzle
res = knn.predict([[30]])
print(res)