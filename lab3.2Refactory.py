p0 = [-1, -1, -1]
p1 = [-1, -1, 1]
p2 = [-1, 1, -1]
p3 = [-1, 1, 1]
p4 = [1, -1, -1]
p5 = [1, -1, 1]
p6 = [1, 1, -1]
p7 = [1, 1, 1]

w = [[1], [1], [1]]
c1 = []
c2 = []

import numpy as numpy

def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1

def clasificator(point):
    prod = numpy.dot(point, w)
    if sgn(prod) == 1:
        return 1
    else:
        return 0

for point in [p0, p1, p2, p3, p4, p5, p6, p7]:
    if clasificator(point):
        c1.append(point)
    else:
        c2.append(point)

print('Clasa 1:', c1)
print('Clasa 2:', c2)
