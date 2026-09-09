

import math
import random
import matplotlib.pyplot as plt


w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x,h):

    summit = False

    while not summit:
         summit= True

         for new_x in range(max(0, x-5), min(100,x+6)):
              if h[new_x] > h[x]:
                   x = new_x
                   summit = False

                   break
    return x


def main(h):

    x0=random.randint(1,98)
    x= climb(x0,h)

    print("startet at %d finished at %d" %(x0,x))

    plt.plot(h)
    plt.plot([x0],h[x0], 'ro')
    plt.plot([x], h[x], 'go')
    plt.plot([x], h[x], 'b^')
    plt.show()
    return(x,x0)

main(h)
