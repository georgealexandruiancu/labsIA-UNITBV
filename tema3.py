import random
import numpy as np

varBase = []
numPicker = []
random = []
newRandom =[]
def copyInBaseTwo(var):
    varTemp = np.base_repr(var, 2)
    if len(varTemp) > 1 and len(varTemp) < 3:
        varTemp = varTemp+"0"
    if len(varTemp) > 0 and len(varTemp) < 3:
        varTemp = varTemp+"00"
    varBase.append(varTemp)
    numPicker.append(0)

    
a1 = [2,1,-1]
fi = [0.0385, 0.0909, 0.0185]
pi = []

length = len(a1)

# init 1 
for i in range(0, length):
     copyInBaseTwo(a1[i])

def makeFIandPI():
    sum = 0
    for j in range(0, len(fi)):
         sum = sum + fi[j]
    for i in range(0, len(fi)):
        pi.append(fi[i]/sum)  


def randomize(var, indexG, mutatie):
    random = var.copy()
    np.random.shuffle(random)
    numPicker[var.index(random[0])] = numPicker[var.index(random[0])] + 1
    # print(random)
    incrucisare(random, indexG, mutatie)

def incrucisare(random, indexG, mutatie):
    newRandom = []
    intreg = np.random.randint(1,3)
    print("intreg = ", intreg)
    index = 0
    while index < len(random)-1:

        #prima parte din primul numar
        tmp00 = random[index][:len(random[index])-intreg]
        #a doua parte din primul numar
        tmp01 = random[index][-intreg:]
    
        #prima parte din al doilea numar
        tmp10 = random[index+1][:len(random[index+1])-intreg]
        #a doua partde din al doilea
        tmp11 = random[index+1][-intreg:]
       
        newRandom.append(tmp00 + tmp11)
        newRandom.append(tmp10 + tmp01)

        index = index + 2
    if mutatie == 1: 
        print("Generatia " , indexG, "cu mutatie de 1 bit : ", newRandom)
    else:
        print("Generatia " , indexG, ": ", newRandom)

# init 2
makeFIandPI() 
mutatieProbabila = 30

indexGeneration = 0
for i in range(100):
  if mutatieProbabila == indexGeneration:
    mutatieA = 1
    randomize(varBase, indexGeneration, mutatieA)
    mutatieProbabila = mutatieProbabila + 30
  else: 
    mutatieA = 0
    randomize(varBase, indexGeneration, mutatieA)
  indexGeneration = indexGeneration + 1 



