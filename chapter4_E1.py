

import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(x_list):
    # add your implementation of the sigmoid function here
    for input in x_list:
        p= 1/(1+math.exp(-input))
        print(p)


list_outputs=[]
for c in c1,c2,c3:
    output= float(c@x)
    # print(output)
    list_outputs.append(output)
    # print(list_outputs)
sigmoid(list_outputs)





# # calculate the output of the sigmoid for x with all three coefficients