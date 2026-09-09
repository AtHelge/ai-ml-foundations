

import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def distance (row1,row2):
    sum=0
    for x,y in zip(row1,row2):
        sum+=abs(x-y)
    return sum

def main(text):
    
    docs = [line.lower().split() for line in text.split('\n')]

    N= len(docs)

    vocabulary = list(set(text.lower().split()))
    
    tf={}
    df={}


    for word in vocabulary:
        tf[word]= [doc.count(word)/len(doc) for doc in docs]
        df[word]= sum([word in doc for doc in docs])/N

    tfidf_matrix = []
    for index, doc in enumerate(docs):
        tfidf_vector = []

        for word in vocabulary:
            tfidf_vector.append(tf[word][index] * math.log(1 / df[word], 10))
        tfidf_matrix.append(tfidf_vector)
      
   
    dist_matrix = [[distance(row1, row2) for row1 in tfidf_matrix] for row2 in tfidf_matrix]
    
    print(dist_matrix)
    dist = np.asarray(dist_matrix, dtype=float)
    np.fill_diagonal(dist, np.inf)

    print("")

    raw_index = np.unravel_index(np.argmin(dist), dist.shape)
    print(raw_index)
    clean_index = (int(raw_index[0]), int(raw_index[1]))
    print("")
    print(clean_index)

main(text)
