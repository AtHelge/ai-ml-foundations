import numpy as np

x_train = np.random.rand(2, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(2,2)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    print(a)
    print(b)
    print("")

    for ai, bi in zip(a, b):
       # print(ai)
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.inf

    for i,a in enumerate(x_train):
        sum=dist(a,x_test)
        #print(i)
        if sum< min_distance:
            min_distance=sum
            nearest = i
    print(nearest)
    
nearest(x_train, x_test)

# def zip2(a,b):
#     for a_onei,b_onei in zip(a,b):
#         print(a_onei)
#         print(b_onei)
#         print("")

# def zipp(x_train,x_test):

#     for a,b in zip(x_train,x_test):
#         print(a)
#         print(b)
#         zip2(a,b)
#         print("")

# zipp(x_train,x_test)