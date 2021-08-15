# Dependencies
import numpy as np

# Data: air quality index AQI data (row = city)
x = np.array(
    [[42,40,41,43,44,43],      # Hong Kong
    [30,31,29,29,29,30],       # New York 
    [8,13,31,11,11,9],         # Berlin 
    [11,11,12,13,11,12]])      # Montreal

cities = np.array(["Hong Kong", "New York", "Berlin", " Montreal"])
print(cities)
print("----------------")

# One-liner
polluted = set(cities[np.nonzero(x > np.average(x))[0]])

# Result
print(polluted)