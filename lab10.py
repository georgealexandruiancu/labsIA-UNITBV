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
    f = (2/(1 + (2.71**(-net)))-1)
    return (f) 

wT = np.array(w)[np.newaxis]
net = np.dot(yp1, wT.T)
print("NET 1 CALCULAT: ", net)

fNET1 = fActivare(net)
print(fNET1)

wT = np.array(w)[np.newaxis]
net = np.dot(yp2, wT.T)
print("NET 2 CALCULAT: ", net)

fNET2 = fActivare(net)
print(fNET2)

def functionVerify(yTest, item, iteration):
    wT = np.array(w)[np.newaxis]
    net = np.dot(yTest, wT.T)
    fNETverification = fActivare(net)
    print(fNETverification)
    if item == 'scaun':
        print("In iteratia: ", iteration, " avem: scaun")
    elif item == 'masa':
        print("In iteratia: ", iteration, " avem: masa")
    elif item == 'pat':
        print("In iteratia: ", iteration, " avem: pat")
    
def calculateItems():
    for i in range(len(yp1)):
        if (yp1[i] - yp2[i]) > 120:
            functionVerify(yp1, 'pat', i)
        elif yp1[i] > yp2[i]:
            functionVerify(yp1, 'masa', i)
        elif yp1[i] < yp2[i]:
            functionVerify(yp2,'scaun', i)

calculateItems()