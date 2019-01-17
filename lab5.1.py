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

#functia de activare dupa formula specificata
def fActivare (net):
    f = (2*(2.71**net))/(np.square(1+(2.71**net)))
    return f

# PAS 1 #
wT = np.array(w)[np.newaxis] #creaza un nou array
net1 = np.dot(x1, wT.T)  #Returnează produsul punct al a și b. Dacă a și b sunt ambele scalare sau ambele matrice 1-D, atunci este returnat un scalar; altfel o matrice este returnată.
print(net1)
for i in xrange(0,len(x1)):
   w2[i] = x1[i] + w[i]
   wF = fActivare(net1) #se apeleaza functia de activare pentru NET
   wF1[i] = wF - x1[i]
print w2



# PAS 2 #
w2T = np.array(w2)[np.newaxis]
net2 = np.dot(x2, w2T.T) ##Returnează produsul punct al a și b. Dacă a și b sunt ambele scalare sau ambele matrice 1-D, atunci este returnat un scalar; altfel o matrice este returnată.
print net2
for i in xrange(0,len(x2)):
   w3[i] = w2[i] - x2[i]
   wF = fActivare(net2) #se apeleaza functia de activare pentru NET
   wF2[i] = wF - x2[i]

print w3



# PAS 3 #
w3T = np.array(w3)[np.newaxis]
net3 = np.dot(x3, w3T.T) ##Returnează produsul punct al a și b. Dacă a și b sunt ambele scalare sau ambele matrice 1-D, atunci este returnat un scalar; altfel o matrice este returnată.
print net3
for i in xrange(0,len(x3)):
   w4[i] = w3[i] - x3[i]
   wF = fActivare(net3) #se apeleaza functia de activare pentru NET
   wF3[i] = wF - x3[i]

print w4


#functii de activare creare NET
fActivare(net1)
fActivare(net2)
fActivare(net3)
#afisare
print "W1 FINAL: \n\n"
for i in xrange(0, len(wF1)):
    print wF1[i]

print "W2 FINAL: \n\n"
for i in xrange(0, len(wF1)):
    print wF2[i]

print "W3 FINAL:  \n\n"
for i in xrange(0, len(wF1)):
    print wF2[i]



