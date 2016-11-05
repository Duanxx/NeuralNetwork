#-*- coding=utf-8 -*-
"""
@file ：activationFunction.py
@author : duanxxnj@163.com
@time : 2016/11/5 17:15
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_sigmoid_function():
    x = np.arange(-10, 10, 0.1)
    y = 1/(1 + np.exp(-x))
    plt.plot(x, y)
    plt.xlim(-10.5, 10.5)
    plt.ylim(-0.1, 1.1)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    plot_sigmoid_function()