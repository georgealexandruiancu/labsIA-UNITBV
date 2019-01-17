
import numpy as np
from PerceptronTema4 import Perceptron

trainingInputs = np.matrix([
    [1, -1, -1],
    [1, -1, -1],
    [1, 1, 1],
])
labels = np.array([
    [1, -1, -1],
])
perceptron = Perceptron(1)
perceptron.train(trainingInputs, labels)

inputs = trainingInputs
perceptron.predict(inputs)

