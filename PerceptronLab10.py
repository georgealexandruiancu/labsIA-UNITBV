import numpy as np

class Perceptron(object):
    #initializare perceptron cu threshold = epoci si learning_rate = rata de invatare
    def __init__(self, no_of_inputs, threshold=200, learning_rate=0.001):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        activation = 1 #initializare activare
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0] #Returnează produsul punct al a și b. Dacă a și b sunt ambele scalare sau ambele matrice 1-D, atunci este returnat un scalar; altfel o matrice este returnată.
        functionNet = (2/(1 + (2.71**(-summation)))-1)
        #functie de activare
        if summation > functionNet:
          activiation = 1
        else:
          activation = -1     
        return activation #se returneaza activarea
    #functie de train pentru perceptron
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
                    prediction = self.predict(inputs) #pe inputul actual parcurs se face o prezicere
                    self.weights[1:] += self.learning_rate * (itemL - prediction) * inputs #se creaza complexitatea pentru fiecare rata de invatare din prezicerea facuta de perceptron
                    self.weights[0] += self.learning_rate * (itemL - prediction)
                    exactPrediction.append(prediction) #se adauga predictiile facute pe varibile
                print("Algoritm predictie: ", exactPrediction)
                # se verifica predictia si se afiseaza in functie de rezultat
                if exactPrediction == [-1, 1, -1]:
                    result = "SCAUN"
                elif exactPrediction == [1,-1 ,-1]:
                    result = "PAT"
                else:
                    result = "MASA"
                exactPrediction = []
                print("For : ",inputs, " we have: ", result)
            print("--------------------------------")
            