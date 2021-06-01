#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:00:11 2021

@author: mahan
"""



import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv(url, names = names)

X = data.values[:, :-1]
y = data.values[:, -1]

kFold = KFold(n_splits=10, shuffle=True, random_state=10)
model = LogisticRegression(solver='liblinear')

score = cross_val_score(model, X, y, cv=kFold, scoring='neg_log_loss')
print(f'score: mean = {score.mean():.3f}; std = {score.std():.2f}')