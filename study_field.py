# Dependencies
from sklearn import tree
import numpy as np

# Data: student scores in (math, languge, crativity) --> study field
x = np.array([[9, 5, 6, "computer science"],
              [1, 8, 1, "linguistics"],
              [5, 7, 9, "art"]])

# One-liner
tree = tree.DecisionTreeClassifier().fit(x[:,:-1], x[:,-1])

# Result & puzzle
student0 = tree.predict([[8, 6, 5]])
print(student0)

student1 = tree.predict([[3, 7, 9]])
print(student1)