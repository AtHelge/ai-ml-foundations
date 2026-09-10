


import numpy as np

# x as feature values for three cabins
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])

# coefficient values
c = np.array([3000, 200 , -50, 5000, 100])

print(X @ c)
print (X)