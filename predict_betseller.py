# Dependencies
import numpy as np

# Dara (row=[title, rating])
books = np.array([['Coffe Break Numpy', 4.6],
                  ['Lord of the rings', 5.0],
                  ['Harry Potter', 4.3],
                  ['Winnie the Pooh', 3.9],
                  ['The clown of god', 2.2],         
                  ['Coffe Break Python', 4.7]])

# One-liner
predict_betseller = lambda x,y : x[x[:,1].astype(float)>y]

# Results
print(predict_betseller(books, 3.9))