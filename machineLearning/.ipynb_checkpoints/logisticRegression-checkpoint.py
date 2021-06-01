#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*** Binary Classification
costFunction = -log(h_theta(x)) if y == 1 else -log(1 - h_theta(x))
             = -y * log(h_theta(x)) - (1-y) * log(1 - h_theta(x))

sigmoid(res) = 1 /(1 + e**(-res))
h_theta(X) = h(X, theta) = sigmoid(X @ theta.transpose)

gradientFunction = (1/m) * (h_theta(X) - y).transpose() @ X.transpose()
"""

import numpy as np
import random
from sklearn.linear_model import LogisticRegression

random.seed(1)

def sigmoid(results):
    return 1 / (1 + np.exp(-results))
    
def makePrediction(theta, X):
    y_pred = sigmoid(X @ theta.T)
    return np.array([1 if x > 0.5 else 0 for x in y_pred])

def getCost(theta, X, y):
    y_pred = sigmoid(X @ theta.T)
    return -(np.average(y * np.log(y_pred)) + np.average((1-y) * np.log(1-y_pred)))

def getTPFPTNFN(y, y_pred):
    y_pred = y_pred.ravel()
    y = y.ravel()
    TP, FP, TN, FN = 0, 0, 0, 0
    for s, s_pred in zip (y, y_pred):
        if s == 1:
            if s_pred == 1: 
                TP += 1
            else:
                FN += 1
        else:
            if s_pred == 0:
                TN += 1
            else:
                FP += 1
    return TP, FP, TN, FN
            

X = np.array([[random.random(), random.random()] for _ in range(100)])
y = np.array([int((2*x[0]+3*x[1]) >= 2.5) for x in X]).reshape(-1, 1)

X = np.concatenate((np.ones([X.shape[0], 1]), X), axis = 1)

theta = np.zeros([1, X.shape[1]])

alpha, m, lam = .1, X.shape[0], 0.1
for i in range(100000):
    # print(getCost(theta, X, y))
    y_pred = sigmoid(X @ theta.T)
    theta -= (alpha/m) * ((y_pred - y).T @ X) + (lam/m) * theta
    
print(theta)

model = LogisticRegression()
model.fit(X, y.ravel())

print(model.coef_)