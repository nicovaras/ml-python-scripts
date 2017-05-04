import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from sklearn.datasets import load_boston
import cvxopt
from data_problems import *

def linear_kernel(xi, xj):
    return np.dot(xi, xj.T)

def gaussian_kernel(xi, xj, sigma=1.):
    return np.exp(-sigma * np.linalg.norm(xi-xj)**2)

def gaussian_fourier_kernel(xi, xj):
    return np.exp(-np.linalg.norm(xi-xj)**2/2.) / np.sqrt(2*np.pi)


def get_kernel_matrix(kernel, n_samples, X):
    K = np.zeros((n_samples, n_samples))
    for i in range(n_samples):
        for j in range(n_samples):
            K[i,j] = kernel(X[i], X[j])
    return K

def solve_dual_problem(K, y, C, n_samples):
    P = cvxopt.matrix(np.outer(y,y) * K)
    q = cvxopt.matrix(np.ones(n_samples) * -1)
    A = cvxopt.matrix(y, (1,n_samples))
    b = cvxopt.matrix(0.0)
    G = cvxopt.matrix(np.vstack((np.diag(np.ones(n_samples) * -1),
                                 np.identity(n_samples))))
    h = cvxopt.matrix(np.hstack((np.zeros(n_samples),
                                 np.ones(n_samples) * C)))

    solution = cvxopt.solvers.qp(P, q, G, h, A, b)
    return np.ravel(solution['x'])

def get_intercept(alpha, support_vectors, support_vectors_y, ind, K):
    b = 0
    for n in xrange(len(alpha)):
        b += support_vectors_y[n]
        b -= np.sum(alpha * support_vectors_y * K[ind[n],support_vectors])
    b /= len(alpha)
    return b

def get_weights(n_features, alpha, support_vectors_x, support_vectors_y):
    w = np.zeros(n_features)
    for n in xrange(len(alpha)):
        w += np.ravel(alpha[n] * support_vectors_y[n] * support_vectors_x[n])
    return w

def fit(X, y, kernel=linear_kernel, C=1.):
    n_samples, n_features = X.shape

    K = get_kernel_matrix(kernel, n_samples, X)
    alpha = solve_dual_problem(K, y, C, n_samples)

    support_vectors = alpha > 1e-5
    ind = np.arange(len(alpha))[support_vectors]
    alpha = alpha[support_vectors]
    support_vectors_x = X[support_vectors]
    support_vectors_y = y[support_vectors]
    print("%d support vectors out of %d points" % (len(alpha), n_samples))

    b = get_intercept(alpha, support_vectors, support_vectors_y, ind, K)
    w = get_weights(n_features, alpha, support_vectors_x, support_vectors_y)

    return support_vectors_x, support_vectors_y, w, b

def plot_margin(w, b, c, k):
    a1 = (-w[0] * -4 - b + c) / w[1]
    b1 = (-w[0] *  4 - b + c) / w[1]
    plt.plot([-4, 4], [a1, b1], k)

def plot_scatter(X, y, X_sv, y_sv):
    plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired)
    plt.xticks(())
    plt.yticks(())
    plt.axis([-3, 3, -3, 3])
    plt.scatter(X_sv[:, 0], X_sv[:, 1], s=50,linewidths=3, marker='s', c=y_sv, cmap=plt.cm.Paired)


def plot(X, y, X_sv, y_sv, w, b):
    plot_scatter(X, y, X_sv, y_sv)
    # plot_margin(w, b, 0, 'k')
    # plot_margin(w, b, 1, 'k--')
    # plot_margin(w, b, -1, 'k--')
    plt.show()

X, y = xor_problem()
X_sv, y_sv, w, b = fit(X, y, kernel=gaussian_fourier_kernel, C=50)
plot(X, y, X_sv, y_sv, w, b)
