import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
LEARNING_RATE = 0.1
gradient_step_points = []

# GD in two variables
def gradient_descent(xs, ys):
    m = len(ys)
    a, b = 0., 0.
    for i in xrange(10000):
        step_a = step_b = 0.
        for x, y in zip(xs, ys):
            step_a += x * (y - (a*x + b))
            step_b += (y - (a*x + b))
        a += LEARNING_RATE * (step_a)/m
        b += LEARNING_RATE * (step_b)/m
        gradient_step_points.append((a,b))
    return a, b

def plot_line(xs, ys, a, b):
    print "{}x + {}".format(a, b)
    plt.plot(xs, ys, 'o', markersize=7)
    plt.plot(xs, [a*x + b for x in xs])

def plot_contour(xs, ys):
    plt.figure()
    plt.plot([x[0] for x in gradient_step_points], [x[1] for x in gradient_step_points], 'o', markersize=3)

    xmesh, ymesh = np.mgrid[-1:3:500j,0:2:500j]
    def f(arr):
        res = np.zeros(arr[0].shape)
        for x, y in zip(xs, ys):
            res += (y - (arr[0]*x + arr[1]))**2
        return res/len(arr[0])
    fmesh = f(np.array([xmesh, ymesh]))
    plt.contour(xmesh,ymesh,fmesh,100)

xs = [0.101, 0.005, 0.06, 0.023, 0.785, 0.12, 0.023, 0.01, 0.55, 0.28, 0.075, 0.122, 0.048, 0.9, 0.104]
ys = [4.0, 0.14, 1.0, 0.3, 3.5, 1.0, 0.4, 0.25, 2.4, 1.9, 1.2, 3.0, 0.33, 2.6, 2.5]

a, b = gradient_descent(xs, ys)
plot_line(xs, ys, a, b)
plot_contour(xs, ys)
plt.show()
