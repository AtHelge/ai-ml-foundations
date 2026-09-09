

import numpy as np

def generate(p1):
    seq= np.random.choice([0,1], p=[1-p1, p1],size=10000)
    return seq

def count(seq):
    count =0
    for i in range(len(seq)-4):
        if seq[i]== 1 and seq[i+1]== 1 and seq[i+2]== 1 and seq[i+3]== 1 and seq[i+4]== 1:
            count+=1
    return count



def main(p1):
    seq= generate(p1)
    return count(seq)

print(main(2/3))

