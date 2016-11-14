#-*- coding=utf-8 -*-
"""
@file ： nn_classification.py
@author : duanxxnj@163.com
@time : 2016/11/11 20:39
"""

from sklearn import datasets
import numpy as np
import time
import matplotlib.pyplot as plt

# 生成测试用的非线性数据
# 这里返回的是最流行的非线性数据之一：双月数据
# @ return X(float in (-1, 1)): 双月数据集 [n_samples, n_features]
#          y(int in {0, 1}): 双月数据对应的标签
def generate_data():
    np.random.seed(int(time.time()%100))
    X, y = datasets.make_moons(200, noise=0.1)
    return X, y

# 显示数据数据集合
def show_data(X, y):
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='r')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='b')
    plt.grid()
    plt.show()

if __name__ == '__main__':

    X ,y = generate_data()
    show_data(X, y)
