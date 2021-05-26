#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:14:26 2021

@author: mahan
"""

#%% Chapter 2

import sklearn.datasets
import matplotlib.pyplot as plt
import numpy as np

#get California housing dataset
data = sklearn.datasets.fetch_california_housing()
X = data.data
y = data.target.reshape(-1, 1)

#scatter plot (latitude, longitude, median income, and cost)
plt.scatter(X[:, 6], X[:, 7], s=y, c=X[:, 0])
plt.colorbar()

X_y = np.concatenate((X, y), axis=1)

#co-variance matrix
cov = np.corrcoef(X_y.T)
ax = plt.matshow(cov)
plt.colorbar()

ticks = data.feature_names + data.target_names
plt.xticks(range(len(ticks)), ticks, rotation=90)
plt.yticks(range(len(ticks)), ticks)

#co-relation plot
n = X_y.shape[1]
fig, axes = plt.subplots(figsize=(n*2, n*2), nrows=n, ncols=n)
for i in range(n):
    for j in range(n):
        plt.sca(axes[i, j])
        if i==n-1: plt.xlabel(ticks[j])
        if j==0: plt.ylabel(ticks[i])
        if i==j:
            da = X_y[:, i]
            plt.hist(X_y[:, i], 
                     bins = np.arange(min(da), max(da), (max(da)-min(da))/20))
        else:
            if i>j:
                plt.scatter(X_y[:, i], X_y[:, j])
            else:
                plt.text(0, 0, f'{cov[i, j]:.2f}')
                plt.xlim([-1, 1])
                plt.ylim([-1, 1])
                plt.axis('off')

import pandas as pd
a = pd.DataFrame(X_y, columns=ticks)
a.info()
a.describe()
a.hist(figsize=(10, 10), bins=50)
pd.plotting.scatter_matrix(a, figsize=(10, 10))


#load from file
file = '/Users/mahan/Documents/learn_python/datasets/housing/housing.csv'
data = pd.read_csv(file)
data.hist(bins=50, figsize=(10,10))

#%%
"""
Frame the problem:
    What is the business objective?
    How company expect to use and benefit from the model?
    
Select a performance measure:
    RMSE, MSE, MAE (Average absolute deviation)
    RMSE:
        Euclidean or l2 norm
    MAE:
        Manhattan or l1 norm
    Higher norm index focusses on the large values

Check the assumptions:
    Help catching serious issues
    
"""

