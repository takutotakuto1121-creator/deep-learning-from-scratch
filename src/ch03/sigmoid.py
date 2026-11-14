import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)


def plt_sigmoid():
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    print("= step_function =")
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()


def plt_ReLU():
    x = np.arange(-5.0, 5.0, 0.1)
    y = ReLU(x)
    print("= step_function =")
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()