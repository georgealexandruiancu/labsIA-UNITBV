x = [2, 1, 2]
y = [1, -1, 4]

import numpy as numpy
import math as math

prod = numpy.dot(x, y)

xLen = math.sqrt(numpy.dot(x, x))
yLen = math.sqrt(numpy.dot(y, y))

print('Produs scalar:', prod)
print('Lungime x:', xLen)
print('Lungime y:', yLen)

angle = math.acos(prod / (xLen * yLen))

print(angle)