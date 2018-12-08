from collections import defaultdict
from random import uniform
from math import sqrt
import random


def point_avg(points):
    """
    - accepta lista de puncte -- pentru fiecare dintre cu dimensiunea identica
    - returneaza un punct care este centrul tuturor punctelor
    """
    dimensions = len(points[0])

    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center


def update_centers(data_set, assignments):
    """
    - accepta lista de seturi si lista de assignments
    - creaza centru pentru fiecare dintre grupuri
    - returneaza k center, unde k este un numar unic de assignments
    """
    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)
        
    for points in new_means.itervalues():
        centers.append(point_avg(points))

    return centers


def assign_points(data_points, centers):
    """
    - se da setul de date si lista cu puncte
    - intre 2 puncte oarecare aduce fiecare punct in indexul care ii corespunde
    - la indexul cel mai apropriat de centru
    - ---
    - returneaza un array de indexuri de centre care corespunde la un index din 
    - dataset
    - ---
    - explicatie: daca sunt X puncte intr-un centru, vor fi X unice posibile
    - valori 
    """
    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    - distanta dintre 2 puncte
    """
    dimensions = len(a)
    
    _sum = 0
    for dimension in range(dimensions):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)


def generate_k(data_set, k):
    """
    - se da datasetul care este un array de arrays
    - gaseste minimul si maximul pentru fiecare coordonat
    - genereaza k - puncte oarecare intre fiecare range
    - returneaza un array de puncte oarecare in range
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in range(k):
        rand_point = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]
            
            rand_point.append(uniform(min_val, max_val))

        centers.append(rand_point)

    return centers


def kMeans(dataset, k):
    """
    - init project
    """
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    print( zip(assignments, dataset) )


points = [
    [45, 85],
    [50, 43],
    [40, 80],
    [55, 42],
    [200, 43],
    [48, 40],
    [195, 41],
    [43, 87],
    [190, 40],
    ]
# newPoints = []
# def myShuffle(array):
#     """
#     - make the points shuffle 
#     """
#     random.shuffle(array)
#     return array
# for index in myShuffle(points):
#     newPoints.append(index)
kMeans(points, 3)