
# to find the nearest neigbough based on text input
#whcih of the text sets are most familiar?
#smallest sum is best
#sum by absolute subtraction of x-y
#first print as 2matrix, new list for each sent 2
# then a float matrix
#removing the diagonals which are 0 cause of comparing with sacme row

import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def distance(row1,row2):
    sum=0
    for x,y in zip(row1,row2):
        sum+= abs(x-y)
    return sum



def find_nearest_pair(data):
    dist_matrix = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    print(dist_matrix)
    dist = np.asarray(dist_matrix, dtype=float)
    print(dist)
    np.fill_diagonal(dist, np.inf)
    raw_index = np.unravel_index(np.argmin(dist), dist.shape)
    clean_index= (int(raw_index[0]),int(raw_index[1]))
    print(clean_index)

find_nearest_pair(data)



