# Dependencies
import numpy as np

# Data: popular Instagram accounts (million followers)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriasecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

# One-liner
superstar = inst[inst[:,0].astype(float)>100,1]

# Results
print(superstar)