#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
y_pred = X * theta.T
cost = (1/2m) * (y_actu - y_pred) ** 2
"""

import numpy as np
import random as r
from sklearn.linear_model import LinearRegression

r.seed(20)

X = []
for x1, x2 in zip([r.random() for _ in range(100)], [r.random() for _ in range(100)]):                                                  
    X.append(np.array([x1, x2]))
    
X = np.array(X)
y = np.array([2*x[0] + 3*x[1] for x in X]).reshape(-1, 1)

ones = np.ones([X.shape[0], 1])
X = np.concatenate((ones, X), axis = 1)

theta = np.zeros((1, X.shape[1]))

def get_cost(X, theta, y):
    diff = y - X @ theta.T
    return 0.5 * np.average(diff ** 2)

alpha, m, lam  = 0.1, X.shape[0], 0.001

for i in range(10000):
    y_pred = X @ theta.T
    theta -= (alpha/m) * (((y_pred - y).T @ X) + lam * theta)
print(theta)


beta = np.linalg.inv(X.T @ X) @ X.T @ y
print (beta)

model = LinearRegression()
model.fit(X, y)

print(model.coef_)


def matmul(X1, X2):
    mat = np.zeros((X1.shape[0], X2.shape[1]))
    
    for i in range(X1.shape[0]):
        for j in range(X2.shape[1]):
            mat[i, j] = sum(X1[i,:] * X2[:,j])
    return mat