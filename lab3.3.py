import numpy as np
import math as math


x = [1,2,3]
y = [0,0,0]

pas = 0
#cat timp x e diferit de y se creaza sign de valorile specificate mai jos
while(x):
    if(xuri ! = 0):
        y[0] = np.sign(x[1]-x[2])
        y[1] = np.sign(x[0]-x[2])
        y[2] = np.sign(-x[0]-x[1])
        pas = pas + 1
    if(pas == len(x)):
        break
    x=y

print y