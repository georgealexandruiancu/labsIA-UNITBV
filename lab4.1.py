import numpy as np 
# 6x^2 + 12x + 1 

#metoda gradientului pe o anumita functie
def Gradient(x):
    length = len(x)
    for i in range(0, length): #parcurge pana la lungimea specificata
        if i < (length-1):
            x[i+1] = x[i] - c * (12 * x[i] + 12) #aduna si creaza complexitatea pentru o anumita functie specificata
    for i in range(0, length): #parcurge pana la lungimea specificata
        print x[i]
        
x = [1,3,4,5,6,7]
c = 0.001

Gradient(x)