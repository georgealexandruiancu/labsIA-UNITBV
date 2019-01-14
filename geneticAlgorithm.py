import random
import numpy as np

def initialize(p_zero, N):
    map = np.zeros((N,N))
    for i in range(0, N):
        for j in range(0, i-1):
            row = []
            if random.random() > p_zero:
                map[i][j] = random.random() * 100
                map[j][i] = map[i][j]
    print(map)
    return map

initialize(0.3, 4)

def createNewMember(maxRoute, N):

    routeLength = random.randint(0, maxRoute)

    for i in range(0, routeLength)

    return member