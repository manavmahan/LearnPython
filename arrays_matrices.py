#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:54:51 2021

@author: mahan
"""
import random as r
import numpy as np
r.seed(10)
X = np.array([[x1, x2] for x1, x2 in zip([r.random() for _ in range(100)], [r.random() for _ in range(100)])])
y = np.array([2 * x[0] + 3 * x[1] for x in X])

def get_cost (X, y, theta):
    return 0.5 * np.average(np.power((X @ theta.T) - y, 2))

def gradient(X, y, theta, learning_rate):
    return learning_rate * np.average((X @ theta.T - y) @ X, axis = 0)
    
def lin_regression(X, y, learning_rate = 0.000001, iteration = 10000):
    ones = np.ones([X.shape[0], 1])
    X = np.concatenate([ones, X], 1)
    
    theta = np.zeros([1, X.shape[1]])
    
    cost = []
    for i in range(iteration):
        theta -= gradient(X, y, theta, learning_rate)
        cost.append(get_cost(X, y, theta))
    return cost, theta

val = lin_regression(X, y)
#beta = np.linalg.inv(np.cross(X_tra, X)) * X_tra * y
