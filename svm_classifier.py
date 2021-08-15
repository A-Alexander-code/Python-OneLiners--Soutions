# Dependencies
from sklearn import svm
import numpy as np

# Data: student scores in (math, language, creativity) --> studuy field
x = np.array([[9, 5, 6, "computer science"],
              [10, 1, 2, "computer science"],
              [1, 8, 1, "computer science"],
              [1, 8, 1, "literature"],
              [4, 9, 3, "literature"],
              [0, 1, 10, "art"],
              [5, 7, 9, "art"]])

# One-liner
svm = svm.SVC().fit(x[:,:-1], x[:,-1])

# Result & puzzle
student0 = svm.predict([[3, 3, 6]])
print(student0)

student1 = svm.predict([[8, 1, 1]])
print(student1)