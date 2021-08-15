# Dependencies
import numpy as np

# Data yearly salary in ($1000) [2017, 2018, 2019]
alice = [99,101,103]
bob = [110,108,105]
tim = [90,88,85]
employees = np.array(["Alice", "Bob", "Tim"])

salaries = np.array([alice,bob,tim])
print(salaries)
print("--------------")
taxation = np.array([[0.2,0.25,0.22],[0.4,0.5,0.4],[0.1,0.2,0.1]])
print(taxation)
print("--------------")

## One-liner
income = salaries - salaries*taxation
print(income)
print("--------------")
max_income = np.max(salaries - salaries*taxation)
max_salary = set(employees[np.nonzero(income > np.average(income))[0]])
# Result
print(max_income)
print(max_salary)