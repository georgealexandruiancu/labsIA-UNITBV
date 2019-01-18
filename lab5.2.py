import numpy as np
import math as math
"""
------------------ VEZI LAB5.1.py
"""
x1 = [1,-2]
x2 = [0,1]
x3 = [2,3]
x4 = [1,-3]
w = [1,-1]
w2 = [0,0]
w3 = [0,0]
w4 = [0,0]
w5 = [0,0]
wF1= [0,0]
wF2= [0,0]
wF3= [0,0]
wF4= [0,0]

def fActivare (net):
    print ("FUNCTIA DE ACTIVARE: ")
    f = (2*(2.71**net))/(np.square(1+(2.71**net)))
    print (f)

# PAS 1 #
wT = np.array(w)[np.newaxis]
net1 = np.dot(x1, wT.T)
print("NET 1: ")
print (net1)
for i in range(0,len(x1)):
   w2[i] = x1[i] + w[i]
   wF = fActivare(net1)
   
print("W 1: ")
print (w2)

# PAS 2 #
w2T = np.array(w2)[np.newaxis]
net2 = np.dot(x2, w2T.T)
print("NET 2: ")
print (net2)
for i in range(0,len(x2)):
   w3[i] = w2[i] - x2[i]
   wF = fActivare(net2)
   
print("W 2: ")
print (w3)

# PAS 3 #
w3T = np.array(w3)[np.newaxis]
net3 = np.dot(x3, w3T.T)
print("NET 3: ")
print (net3)
for i in range(0,len(x3)):
   w4[i] = w3[i] - x1[i]
   wF = fActivare(net3)
   
print("W 3: ")
print (w4)

# PAS 4 #
w4T = np.array(w4)[np.newaxis]
net4 = np.dot(x4, w4T.T)
print("NET 4: ")
print (net4)
for i in range(0,len(x3)):
   w5[i] = w4[i] - x4[i]
   wF = fActivare(net4)
   

print("W 4: ")
print (w5)


    
fActivare(net1)
fActivare(net2)
fActivare(net3)
fActivare(net4)

