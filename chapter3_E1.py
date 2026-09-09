

#using numpy -> easy match of integers for indizez and multiply and sum of all


import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])

# coefficient values
c = np.array([3000, 200 , -50, 5000, 100])

print(X @ c)
print (X)