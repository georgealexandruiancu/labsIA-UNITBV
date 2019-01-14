import numpy as np
import math
"""
    - initializare 
"""
w1  = [70,80]
w2 = [75,50]
w3 = [120,48]
w1Copy  = [70,80]
w2Copy = [75,50]
w3Copy = [120,48]
 
k = 0
c = 0.1
 
l = [45,50,40,55,200,48,195,43,190]
i = [85,43,80,42,43,40,41,87,40]
"""
    - ./initializare 
"""
def activate(l, w, i, w1, index):
    return math.sqrt((l[index] - w[0])**2 +(i[index] - w1[1])**2)

def calculateM(w, c, l, wC, index):
    return w[0] + c*(l[index] - wC[0])

def calculateN(w, c, l, wC, index):
    return w[1] + c*(l[index] - wC[1])

def ViewEpocs(k, w1, w2, w3):
    print("----------------------")
    print("Epoca: ", k)
    print("w1 final este")
    print(w1)
    print("w2 final este")
    print(w2)
    print("w3 final este")
    print(w3)


while k < 3:
    for index in range(0,9):
        det1 = activate(l, w1, i, w1, index)
        det2 = activate(l, w2, i, w2, index)
        det3 = activate(l, w3, i, w3, index)

        if det1 < det2 and det1 < det3:
            M = calculateM(w1, c, l, w1Copy, index)
            N = calculateN(w1, c, l, w1Copy, index) 
            w1[0] = M
            w1[1] = N

        elif det2 < det1 and det2 < det3:
                    M = calculateM(w2, c, l, w2Copy, index)
                    N = calculateN(w2, c, l, w2Copy, index) 
                    w2[0] = M
                    w2[1] = N

        elif det3 < det1 and det3 < det2:
                        M = calculateM(w3, c, l, w3Copy, index)
                        N = calculateN(w3, c, l, w3Copy, index) 
                        w3[0] = M
                        w3[1] = N
                        k += 1

                        ViewEpocs(k, w1, w2, w3)
      