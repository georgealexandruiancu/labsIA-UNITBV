import numpy as np 
# 6x^2 + 12x + 1 
def Gradient(x):
    length = len(x)
    for i in range(0, length):
        if i < (length-1):
            x[i+1] = x[i] - c * (12 * x[i] + 12)
    for i in range(0, length):
        print x[i]
        
x = [1,3,4,5,6,7]
c = 0.001

Gradient(x)