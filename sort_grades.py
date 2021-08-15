# Dependencies
import numpy as np

# Data SAT scores dor different students
sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])

# One-liner
top_3 = students[np.argsort(sat_scores)[:-4:-1]]

# Result
print(top_3)