#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cost = -y log(y_pred) - (1-y) log(1-y_pred)

l = number of layers
thetas = list(l - 1) (0, 1, 2, ..., l-1)
thetas[l-1] = matrix(neurons[l] X neurons[l-1] + 1)
*** theta[l-1] is mapping from layer[l-1] to layer[l] (nothing from last layer)


*** calculated for all the layers
activatations[l] =  X                                           if l==0
                    activate(X @ thetas[l-1].T)                 if l==1
                    activate(activations[l-1] @ thetas[l-1].T)  if l>1 
                    
***  difference calcualted for layer (except first layer)
difference[l] =     y - activations[l]                                                              if l==len(thetas)
                    (difference[l+1] @ theta[l]) * activate(activations[l] * (1 - activataions[l]))   otherwise

gradient[l-1] =     difference[l].T @ activations[l-1]


********* detailed example **********
first (input) layer
neurons = 8 (excl. bias)                            activations[0] = matrix(m X 9)

second layer
neurons = 3          theta[0] = matrix(3 X 9)       activations[1] = matrix(m X 4)

third layer
neurons = 2          theta[1] = matrix(2 X 4)       activations[2] = matrix(m X 3)

fourth (output) layer
neurons = 1          theta[2] = matrix(1 X 3)       activations[3] = matrix(m X 1)  *(no bias)
"""

import requests
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

url = "https://gist.githubusercontent.com/ktisha/c21e73a1bd1700294ef790c56c8aec1f/raw/819b69b5736821ccee93d05b51de0510bea00294/pima-indians-diabetes.csv"

tData = requests.get(url).text

data = []

for l in tData.split('\n'):
    if l[0]!='#':
        data.append([float(x) for x in l.split(',')])
    
data = np.array(data)
scalar = MinMaxScaler()

X = scalar.fit_transform(data[:, :-1])
y = data[:, -1].reshape(-1, 1)

ones = np.ones((X.shape[0], 1))
X = np.concatenate((ones, X), axis = 1)

nNeurons = [X.shape[1] - 1, 12, 1]

alpha = 0.002; lam = 0.001

def activate(r, activation = 'sigmoid'):
    return 1 / (1 + np.exp(-r))

def getCost(y_acat, y_pred):
    return np.average((-y_acat * np.log(y_pred)) - (1 - y_acat) * np.log(1 - y_pred))

def initialise(nNeurons):    
    thetas = []   
    for n in range(0, len(nNeurons) - 1):
        thetas.append(np.random.rand(nNeurons[n+1], nNeurons[n] + 1))       
    return thetas

def predict(theta, X):
    activations = [];
    activations.append(X)
    for l in range(1, len(theta) + 1):
        activation = activate(activations[l-1] @ theta[l-1].T)       
        if l < len(theta):
            ones = np.ones((activation.shape[0], 1))
            activation = np.concatenate((ones, activation), axis = 1)
        activations.append(activation)
    return [int(x>0.5) for x in activations[-1]]

def getCostAndGradient(theta, X, y):
    activations = []; gradients = []
    activations.append(X)
    for l in range(1, len(theta) + 1):
        activation = activate(activations[l-1] @ theta[l-1].T)       
        if l < len(theta):
            ones = np.ones((activation.shape[0], 1))
            activation = np.concatenate((ones, activation), axis = 1)
        activations.append(activation)
    
    while l>0:
        if l == len(theta):
            diff = y - activations[l]
        else:
            if l<len(theta) - 1:
                diff = diff[:, 1:]
            diff = (diff @ theta[l]) * (activations[l] * (1 - activations[l]))
        
        grad = diff.T @ activations[l-1]
        grad = grad if l == len(theta) else grad[1:,:]
        gradients.append(grad)
        l -= 1
    gradients.reverse()
    
    return getCost(y, activations[-1]), gradients
        
theta = initialise(nNeurons)
for i in range(1000):
    cost, gradients = getCostAndGradient(theta, X, y)
    print(cost)
    for x, t in enumerate(theta):
        theta[x] += alpha * gradients[x] - (lam/X.shape[0]) * theta[x]
        
y_pred = predict(theta, X)
print('score: ', accuracy_score(y, y_pred))
