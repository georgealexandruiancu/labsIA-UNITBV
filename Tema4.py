
import numpy as np
from PerceptronTema4 import Perceptron

trainingInputs = np.array([
    [1, -1, -1],
    [1, -1, -1],
    [1, 1, 1],
])
trainingInputsI = np.array([
    [1, -1, -1],
    [1, -1, -1],
    [1, -1, -1],
])
labels = np.array([
    [1, -1, -1],
])
#pentru litera L
perceptron = Perceptron(3)
perceptron.train(trainingInputs, labels)

inputs = trainingInputs
perceptron.predict(inputs)
#pentru litera I
# perceptron = Perceptron(3)
# perceptron.train(trainingInputsI, labels)

# inputs = trainingInputsI
# perceptron.predict(inputs)

