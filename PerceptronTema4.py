import numpy as np

class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.001):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        activation = 1
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        functionNet = (2/(1 + np.power(2.71,(-summation)))-1)
        if summation > functionNet:
          activiation = 1
        else:
          activation = -1     
        return activation

    def train(self, training_inputs, labels):
        print("------------------------")
        print("FINISH FITNESS")
        print("Start prediction")
        print("------------------------")
        result = ""
        for _ in range(self.threshold):
            print("--------------------------------")
            print("Epoca :", _)
            for inputs, label in zip(training_inputs, labels):
                exactPrediction = []
                for itemL in label:
                    print(itemL)
                    # prediction = self.predict(inputs)
                    # print(itemL)
                    # self.weights[1:] += self.learning_rate * (itemL - prediction) * inputs
                    # self.weights[0] += self.learning_rate * (itemL - prediction)
                    # exactPrediction.append(prediction)
                print("Algoritm prediction: ", exactPrediction)
               
                if exactPrediction == [1, -1, -1]:
                    result = "Litera L"
                else:
                    result = "Nu e L"
                exactPrediction = []
                print("For : ",inputs, " we have: ", result)
            print("--------------------------------")
            