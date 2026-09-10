import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main(train_file, test_file):

    # print(train_file)
    # print("")
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    

    xy_train = np.genfromtxt(train_file)
    x_train = xy_train[:,:-1]

    y_train = xy_train[:,-1]

     
    #linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train,y_train)[0]
    

    #read in the test data and separate x_test from it
    #version 1
    xy_test = np.genfromtxt(test_file)
    x_test= xy_test[:,:-1]
    # print(x_test)
    # print(" ")


    # version 2
    # x_test2= np.asarray([[36, 3 ,15, 1, 850 ],
    #                     [75 ,5 ,18 ,2 ,540 ]])
    # print(x_test2)
    # print("")

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)
    # print(" ")
    # print(x_test2@c)
 

train_file = StringIO(train_string)
test_file = StringIO(test_string)
main(train_file,test_file)
