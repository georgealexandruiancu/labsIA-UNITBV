import numpy as np
import math as math

x1 = [1, -2, 1.5, 0]
x2 = [1, -0.5, -2, -1.5]
x3 = [0, 1, -1, 1.5]
w = [1, -1, 0, 1.5]
w2 = [0,0,0,0]
w3 = [0,0,0,0]
w4 = [0,0,0,0]
wF1= [0,0,0,0]
wF2= [0,0,0,0]
wF3= [0,0,0,0]


def fActivare (net):
    f = (2*(2.71**net))/(np.square(1+(2.71**net)))
    return f

# PAS 1 #
wT = np.array(w)[np.newaxis]
net1 = np.dot(x1, wT.T)
print(net1)
for i in xrange(0,len(x1)):
   w2[i] = x1[i] + w[i]
   wF = fActivare(net1)
   wF1[i] = wF - x1[i]
print w2



# PAS 2 #
w2T = np.array(w2)[np.newaxis]
net2 = np.dot(x2, w2T.T)
print net2
for i in xrange(0,len(x2)):
   w3[i] = w2[i] - x2[i]
   wF = fActivare(net2)
   wF2[i] = wF - x2[i]

print w3



# PAS 3 #
w3T = np.array(w3)[np.newaxis]
net3 = np.dot(x3, w3T.T)
print net3
for i in xrange(0,len(x3)):
   w4[i] = w3[i] - x3[i]
   wF = fActivare(net3)
   wF3[i] = wF - x3[i]

print w4



fActivare(net1)
fActivare(net2)
fActivare(net3)
print "W1 FINAL: \n\n"
for i in xrange(0, len(wF1)):
    print wF1[i]

print "W2 FINAL: \n\n"
for i in xrange(0, len(wF1)):
    print wF2[i]

print "W3 FINAL:  \n\n"
for i in xrange(0, len(wF1)):
    print wF2[i]



