import numpy as np 
import random
from math import pow
import matplotlib.pyplot as plt

# P1: 45 85
# P2: 50 43
# P3: 40 80
# P4: 55 42
# P5: 200 43
# P6: 48 40
# P7: 195 41
# P8: 43 87
# P9: 190 40
p1 = [45,50,40,55,200,48,195,43,190]
p2 = [85, 43, 80, 42, 43, 40, 41, 87, 40]
newP1 = []
newP2 = []
def myShuffle(array):
    random.shuffle(array)
    return array

for index in myShuffle(p1):
    newP1.append(index)
for index in myShuffle(p2):
    newP2.append(index)

print newP1
print newP2

# Set three centers, the model should predict similar results
center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

# Generate random data and center it to the three centers
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

data = np.concatenate((data_1, data_2, data_3), axis = 0)

plt.scatter(data[:,0], data[:,1], s=7)