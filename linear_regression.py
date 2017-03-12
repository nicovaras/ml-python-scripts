import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from sklearn.datasets import load_boston


LEARNING_RATE = 0.1
gradient_step_points = []

# GD in two variables
def gradient_descent(xs, ys):
    m = len(ys)
    a, b = 2., 2.
    for i in xrange(1000):
        step_a = step_b = 0.
        for x, y in zip(xs, ys):
            step_a += x * (y - (a*x + b))
            step_b += (y - (a*x + b))
        a += LEARNING_RATE * (step_a)/m
        b += LEARNING_RATE * (step_b)/m
        gradient_step_points.append((a,b))
    return a, b

def normalize(arr):
    min_val, max_val = min(arr), max(arr)
    return [ (x-np.mean(arr))/(max_val-min_val) for x in arr ]

def plot_line(xs, ys, a, b):
    print "{}x + {}".format(a, b)
    plt.plot(xs, ys, 'o', markersize=7)
    plt.plot(xs, [a*x + b for x in xs])

def plot_contour(xs, ys):
    plt.figure()
    plt.plot([x[0] for x in gradient_step_points], [x[1] for x in gradient_step_points], 'o', markersize=3)

    xmesh, ymesh = np.mgrid[-5:5:50j,-5:5:50j]
    def f(arr):
        res = np.zeros(arr[0].shape)
        for x, y in zip(xs, ys):
            res += (y - (arr[0]*x + arr[1]))**2
        return res/len(arr[0])
    fmesh = f(np.array([xmesh, ymesh]))
    plt.contour(xmesh,ymesh,fmesh,50)

def plot_learning_rates(xs, ys):
    global LEARNING_RATE, gradient_step_points
    plt.figure()
    plt.ylim((0,0.002))
    for rate in [10., 1., 0.1, 0.01, 0.001, 0.0001]:
        LEARNING_RATE = rate
        gradient_step_points = []
        gradient_descent(xs, ys)
        alphas = [x[0] for x in gradient_step_points]
        plt.plot(range(len(alphas) - 1),
                 [abs(alphas[i] - alphas[i-1]) for i in range(1, len(alphas))],
                 'o')


boston_x, boston_y = load_boston(True)
xs = normalize(boston_x[:,8])
ys = normalize(boston_x[:,9])
a, b = gradient_descent(xs, ys)
plot_line(xs, ys, a, b)
plot_contour(xs, ys)
plot_learning_rates(xs,ys)
plt.show()
