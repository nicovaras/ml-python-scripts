import math
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

LEARNING_RATE = 0.2

def logistic(theta, x):
    # log logistic
    theta = theta.reshape(len(theta), 1)
    x = x.reshape(len(x), 1)
    z = theta.T.dot(x)
    if -z < 200:
        return 1./(1 + math.exp(-z))
    else:
        return 0.

def cost_function(theta, x, y):
    return (y - logistic(theta, x))

def gradient_descent(xs, ys):
    feature_lenght = len(xs[0])
    m = len(xs)
    theta = np.array([0.] * feature_lenght)

    for _ in xrange(100):
        step_theta = np.array([0.] * feature_lenght)
        for i in xrange(len(ys)):
            cost = cost_function(theta, xs[i], ys[i])
            step_theta += xs[i] * cost
        theta += LEARNING_RATE * (step_theta)/m
    return theta

def map_features(f1, f2, order=1):
    def iterate():
        for i in range(1, order + 1):
            for j in range(i + 1):
                yield np.power(f1, i - j) * np.power(f2, j)
    return np.vstack(iterate())


def run():
    classes = 2
    order = 3
    X, y = make_classification(600, classes, classes, 0, random_state=15)
    X =  map_features(X[:,0], X[:,1], order).T
    for i in range(len(y)):
        if X[i][0] > 0:
            y[i] = 2

    estimator = LogisticRegression()
    estimator.fit(X, y)

    X = np.c_[np.ones(len(X)), X]
    print estimator.coef_, estimator.intercept_

    thetas = []
    for i in range(classes+1):
        yhat = np.copy(y)
        for j in xrange(len(yhat)):
            if yhat[j] != i:
                yhat[j] = i + 1

        for j in xrange(len(yhat)):
            if yhat[j] == i:
                yhat[j] = 0

        for j in xrange(len(yhat)):
            if yhat[j] != 0:
                yhat[j] = 1

        thetas.append(gradient_descent(X, yhat))

    print thetas
    colors = [(0.,0.,1.), (0.,0.,0.), (1.,0.,0.)]
    for i in range(classes+1):
        dim = np.linspace(-5, 5, 50)
        dx, dy = np.meshgrid(dim, dim)
        v = map_features(dx.flatten(), dy.flatten(), order=order)
        z = (np.dot(thetas[i][1:], v) + thetas[i][0]).reshape(50, 50)
        plt.scatter(X[:,1], X[:, 2], c=y, s=50, cmap='bwr')
        plt.contour(dx,dy,z,1,colors=[colors[i]], linewidths=2)

    plt.show()
run()
