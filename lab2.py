import csv

myList = []
"""
-----
Comanda deschidere fisier 
libraria csv e folosita pentru parsarea fisierului
delimiter - ajuta la impartirea pe linii si coloane csv
"""
with open('./iris.data') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        if len(row) == 5:
            myList.append([float(row[0]), float(row[1]),
                           float(row[2]), float(row[3])])

import numpy as np

npArray = np.array(myList) #creaza un obiect cu lista importata din csv


min = []
max = []
average = []
median = []

norm = [0.2, 1.1, -0.9, 1]
norm_values = []
new_array = []

for i in range(4):
    min.append(np.min(npArray[:, i]))  #creaza minimul parsand cu i
    max.append(np.max(npArray[:, i]))  #creaza maximul parsand cu i
    average.append(np.average(npArray[:, i])) #pune in vector media 
    median.append(np.median(npArray[:, i])) #pune in vector si calculeaza mediana de-a lungul axei


#functie normalizare 
for column in npArray:
    norm_value = []

    i = 0
    weighted_average = 0

    for elem in column:
        norm_value.append((elem - min[i]) / (max[i] - min[i]))
        weighted_average = weighted_average + elem * norm[i]

        i = i + 1

    new_array.append(np.append(column, weighted_average))
    norm_values.append(norm_value)


print('min:', min, '\n')
print('max:', max, '\n')
print('average:', average, '\n')
print('median:', median, '\n')
print('norm values:', np.array(norm_values), '\n')
print('array:', np.array(new_array), '\n')
