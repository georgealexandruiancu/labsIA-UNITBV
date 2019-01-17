
import numpy as np
from PerceptronLab10 import Perceptron

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
perceptron = Perceptron(3)
perceptron.train(trainingInputs, labels)

inputs = trainingInputs
perceptron.predict(inputs)

