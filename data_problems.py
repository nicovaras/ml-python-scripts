import numpy as np

def xor_problem():
    rng = np.random.RandomState(42)
    X = rng.randn(300, 2)
    y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
    return X, y

def linear_problem():
    rng = np.random.RandomState(42)
    X = rng.randn(600, 2)
    X[X[:, 0] > 0] += 0.25
    X[X[:, 0] < 0] -= 0.25
    y = X[:, 0] > 0

    theta = np.radians(30)
    c, s = np.cos(theta), np.sin(theta)
    R = np.matrix([[c, -s], [s, c]])

    return X*R, y
