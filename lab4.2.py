import numpy as np 
from math import pow
# 6x^2 + 12x + 1 
def GradientDoubleG(x, y):
    length = len(x)
    for i in range(0, length):
        if i < (length-1):
            x[i+1] = x[i] - c * (2 * x[i] + 2*(y[i]*y[i]))
            y[i+1] = y[i] - c * (2 * (x[i]*x[i]) + 4*y[i])
    for i in range(0, length):
        print ("x: {} , y: {}".format(x[i],y[i]))
def GradientDoubleH(x,y):
        length = len(x)
        for i in range(0, length):
                if i < (length - 1):
                        x[i+1] = x[i] - c * ( 2*x[i] + 2 + 100*pow((x[i] - pow(y[i],2)),2))
                        y[i+1] = y[i] - c * (pow((1-x[i]), 2) + 100*pow((x[i] - 2*y[i]),2))  
        for i in range(0, length):
                print ("x: {} , y: {}".format(x[i],y[i]))
               
x = [1,3,4,5,6,7]
y = [3,5,7,9,11,13]
c = 0.001

GradientDoubleG(x, y)
GradientDoubleH(x, y)

