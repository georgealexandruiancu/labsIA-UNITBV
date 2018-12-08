import numpy as np
import math as math

x = [2,1,2]
y = [1,-1,4]
SclarProduct = 0
noRadX = 0
noRadY = 0
print ("First array: ")
print x

print ("Second array: ")
print y
# PRODUS SCALAR -----
for i, j in zip(x,y):
    print (i,j)
    SclarProduct += i * j

print("Produsul sclar: ")
print SclarProduct

# LUNGIMEA VECTORULUI -----
for i in x:
    noRadX += i*i

lungX = math.sqrt(noRadX)
print ("lungX: {:.2f}".format(lungX))


for j in y:
    noRadY += j*j

lungY = math.sqrt(noRadY)
print ("lungY: {:.2f}".format(lungY))

#COSINUSUL ------
cos = (SclarProduct)/((lungX)*(lungY))
print cos
