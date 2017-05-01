import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from sklearn.datasets import load_boston
from cvxopt import matrix, solvers
from data_problems import *

def linear_kernel(xi, xj):
    return xi.dot(xj)

X, y = linear_problem()
# plot
plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired)
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
