import numpy as np
import math as math
"""
---------- VEZI LABORATORUL 4 si 5 !
"""
w1 = [0,1,0]
x1 = [2,1,-1]
d1 = -1
wT = []
x2 = [0,-1,-1]
d2 = 1

w2 = [0,0,0]
w3 = [0,0,0]
w4 = [0,0,0]

wF1= [0,0,0]
wF2= [0,0,0]
wF3= [0,0,0]

i = 0

# def Test():
#     wTest = [1,-1,0,0.5]
#     xTest = [1,-2,0,-1]
#     wT = np.array(wTest)[np.newaxis]
#     net1 = np.dot(xTest, wT.T)
#     print(net1)

# REPETATI SECVENTA DE INSTRUIRE (x1,d1) , (x2,d2) pana cand se obtin raspunsurile corecte. Listati valorile net^K obtinute.

def fActivare (net):
    f = (2*(2.71**net))/(np.square(1+(2.71**net)))
    return f

def passing1(x, w):
        # PAS 1 #
        wT = np.array(w)[np.newaxis]
        net1 = np.dot(x, wT.T)
        for i in range(0,len(x)):
            w2[i] = x[i] + w[i]
            wF = fActivare(net1)
            wF1[i] = wF - x[i]

         # PAS 2 #
        w2T = np.array(w2)[np.newaxis]
        net2 = np.dot(x, w2T.T)
        for i in range(0,len(x)):
            w3[i] = w2[i] - x[i]
            wF = fActivare(net2)
            wF2[i] = wF - x[i]

        # PAS 3 #
        w3T = np.array(w3)[np.newaxis]
        net3 = np.dot(x, w3T.T)
        for i in range(0,len(x)):
            w4[i] = w3[i] - x[i]
            wF = fActivare(net3)
            wF3[i] = wF - x[i]

        fActivare(net1)
        fActivare(net2)
        fActivare(net3)
        if (wF1 + wF2) > wF3:
            print ("W1 FINAL: \n")
            for i in range(0, len(wF1)):
                print (wF1[i])
            print ("\n")

            print ("W2 FINAL: \n")
            for i in range(0, len(wF1)):
                print (wF2[i])
            print ("\n")

            print ("W3 FINAL:  \n")
            for i in range(0, len(wF1)):
                print (wF2[i])
            print ("\n")
        

print("First parsing x1,w1 \n\n")
passing1(x1, w1)
print("Second parsing x2,w1 \n\n")
passing1(x2, w1)
