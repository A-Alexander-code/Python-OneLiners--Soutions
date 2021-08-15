# Dependencies
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Data students scores in (math, language, crativity) --> study field
x = np.array([[9, 5, 6, "computer science"],
              [5, 1, 5, "computer science"],
              [8, 8, 8, "computer science"],
              [1, 10, 7, "literature"],
              [1, 8, 1, "literature"],
              [5, 7, 9, "art"],
              [1, 1, 6, "art"]])

# One-liner
forest = RandomForestClassifier(n_estimators = 10).fit(x[:,:-1], x[:,-1])

# Result
students = forest.predict([[8, 6, 5],
                           [3, 7, 9],
                           [2, 2, 1]])
print(students)