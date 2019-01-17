import numpy as np
import math as math

x = [2,1,2]
a = [1,1,1]
p = 0

#compunere de vectori si produs 
for i in x:
    w = x[i] * a[i]
    p = p + a[i]

print(np.sign(p)) #creaza signum returneaza 1 / -1