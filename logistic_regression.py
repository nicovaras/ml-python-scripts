import math
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

LEARNING_RATE = 2

def logistic(theta, x):
    theta = theta.reshape(len(theta), 1)
    x = x.reshape(len(x), 1)
    z = theta.T.dot(x)
    if -z < 200:
        return 1./(1 + math.exp(-(z)))
    else:
        return 0.

def cost_function(theta, x, y):
    return (y - logistic(theta, x))

# GD in two variables
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
    X, y = make_classification(200, 2, 2, 0, weights=[.5, .5], random_state=150)
    X =  map_features(X[:,0], X[:,1], 8).T

    estimator = LogisticRegression()
    estimator.fit(X, y)

    X = np.c_[np.ones(len(X)), X]
    theta = gradient_descent(X, y)
    print estimator.coef_, estimator.intercept_
    print theta
    dim = np.linspace(-5, 5, 50)
    dx, dy = np.meshgrid(dim, dim)
    v = map_features(dx.flatten(), dy.flatten(), order=8)
    z = (np.dot(theta[1:], v) + theta[0]).reshape(50, 50)
    z2 = (np.dot(estimator.coef_, v) + estimator.intercept_).reshape(50, 50)

    plt.scatter(X[:,1], X[:, 2], c=y[:], s=50, cmap='bwr')
    plt.contour(dx,dy,z,1)
    plt.show()

run()
