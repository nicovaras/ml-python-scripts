import math
import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

LEARNING_RATE = 0.001

def perceptron(theta, x):
    z = theta.T.dot(x)
    if  z >= 0.0:
        return 1
    else:
        return -1


def cost_function(theta, x, y):
    return (y - perceptron(theta, x))

def gradient_descent(xs, ys):
    feature_lenght = len(xs[0])
    theta = np.array([0.] * feature_lenght)

    for _ in xrange(100):
        for i in xrange(len(ys)):
            cost = LEARNING_RATE * cost_function(theta, xs[i], ys[i])
            theta += xs[i] * cost
    return theta


def run():
    X, y = make_classification(200, 2, 2, 0, weights=[.5, .5], random_state=150)
    X = np.c_[np.ones(len(X)), X]
    y = np.where(y == 0, -1, 1)
    theta = gradient_descent(X, y)
    x1 = np.linspace(-5, 5, 100)*theta[2]*len(X)
    x2 = np.linspace(-5, 5, 100)*theta[1]*len(X)
    plt.axis((-5,5,-5,5))

    plt.scatter(X[:, 1], X[:, 2], c=y[:], s=50, cmap='bwr')
    plt.plot(np.linspace(-5, 5, 100), x1 + x2 + theta[2])

    plt.figure()
    plt.axis((-5,5,-5,5))

    yhat = []
    for i in range(len(X)):
        x = X[i]
        z = theta.T.dot(x)
        if  z >= 0:
            yhat.append(1)
        else:
            yhat.append(-1)


    plt.scatter(X[:, 1], X[:, 2], c=yhat, s=50, cmap='bwr')
    plt.plot(np.linspace(-5, 5, 100), x1 + x2 + theta[2])

    plt.show()

run()
