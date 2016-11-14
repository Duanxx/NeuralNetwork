#-*- coding=utf-8 -*-
"""
@file ：activationFunction.py
@author : duanxxnj@163.com
@time : 2016/11/5 17:15
"""

import matplotlib.pyplot as plt
import numpy as np


# sigmoid function
# input :x array like
# return 1/(1+exp(x))
def sigmoid(x):
    x = np.array(x)
    y = 1.0/(1.0 + np.exp(-x))
    return y


# sigmoid function
# input :x array like
# return ln(1 + exp(x))
def rectifier(x):
    x = np.array(x)
    y = np.log(1 + np.exp(x))
    return y


# plot the activation function
def plot_activation_function(activation_func, xr=[-5, 5]):
    x = np.arange(xr[0], xr[1], 0.1)
    y = activation_func(x)
    plt.plot(x, y)
    plt.plot(x*0, x, c='r')
    plt.plot(x, x*0, c='r')
    plt.xlim(x.min() - 0.1, x.max() + 0.1)
    plt.ylim(y.min() - 0.1, y.max() + 0.1)
    plt.grid()


if __name__ == '__main__':
    plt.figure(1)
    plot_activation_function(sigmoid)

    plt.figure(2)
    plot_activation_function(np.tanh)

    plt.figure(3)
    plot_activation_function(rectifier)

    plt.show()
