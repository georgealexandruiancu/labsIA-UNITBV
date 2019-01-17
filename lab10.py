
import numpy as np
from PerceptronLab10 import Perceptron
#initializare variabile
trainingInputs = np.array([
    [45, 85, -1],
    [50, 43, -1],
    [40, 80, -1],
    [55, 42, -1],
    [200, 43, -1],
    [48, 40, -1],
    [195, 41, -1],
    [43, 87, -1],
    [190, 40, -1]
])
labels = np.array([
    [1, -1, -1],
    [-1, 1, -1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, -1],
    [-1, -1, 1]
])
#creare obiect cu dimensiunea de 3 in acest caz
perceptron = Perceptron(3)
#apelare functie de instruire perceptron din obiectul Perceptron vezi PerceptronLab10.py
perceptron.train(trainingInputs, labels)
#initializare inputs pentru prezicere
inputs = trainingInputs
#apelare functie de prezicere din obiectul Perceptron vezi PerceptronLab10.py
perceptron.predict(inputs)

