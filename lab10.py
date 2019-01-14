import random
import numpy as np
import math as math

yp1 = [45,50,40,55,200,48,195,43,190]
yp2 = [85,43,80,42,43,40,41,87,40]
yp3 = -1
w = [
    [1, -1, 1],
    [-1, 1, -1],
    [1 ,-1 ,-1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, -1 ,1],
    [1, -1, -1],
    [-1, -1, 1]
    ]
wF1 = []
w2 = []
def fActivare (net):
    print ("FUNCTIA DE ACTIVARE: ")
    f = (2*(2.71**net))/(np.square(1+(2.71**net)))
    print (f)

wT = np.array(w)[np.newaxis]
net = np.dot(yp1, wT.T)
print(net)
fActivare(net)