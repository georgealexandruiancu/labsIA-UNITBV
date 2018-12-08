
import numpy as np

def gradient_descent(x,y):

    m_current = b_current = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.0001

    for i in range(iterations):
        y_predicted = m_current * x + b_current
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_current = m_current - learning_rate * md
        b_current = b_current - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_current,b_current,cost, i))

x = np.array([1,2,3,4,5])
# print x
y = np.array([5,7,9,11,13])
# print y
gradient_descent(x,y)