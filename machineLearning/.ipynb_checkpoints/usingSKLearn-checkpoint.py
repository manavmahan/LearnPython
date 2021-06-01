#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import requests
from sklearn.metrics import accuracy_score
import gzip



url = "https://gist.githubusercontent.com/ktisha/c21e73a1bd1700294ef790c56c8aec1f/"
url += "raw/819b69b5736821ccee93d05b51de0510bea00294/pima-indians-diabetes.csv"

dPath = '/Library/WebServer/Documents/p-EnergyAnalysis/learn_python/datasets/mnist/'

image_size = 28
n_train = 50000
n_test = 10000

train_X_gzip = gzip.open(f'{dPath}/train-images-idx3-ubyte.gz', 'r')
buffer_train_X = train_X_gzip.read(image_size * image_size * n_train)
data_train_X = np.frombuffer(buffer_train_X, dtype = np.uint8)
data_train_X = data_train_X.reshape(n_train, image_size*image_size)

train_y_gzip = gzip.open(f'{dPath}/train-labels-idx1-ubyte.gz', 'r')
buffer_train_y = train_y_gzip.read(n_train)
data_train_y = np.frombuffer(buffer_train_y, dtype = np.uint8)

test_X_gzip = gzip.open(f'{dPath}/t10k-images-idx3-ubyte.gz', 'r')
buffer_test_X = test_X_gzip.read(image_size * image_size * n_test)
data_test_X = np.frombuffer(buffer_test_X, dtype=np.uint8)
data_test_X = data_test_X.reshape(n_test, image_size * image_size)

test_y_gzip = gzip.open(f'{dPath}/t10k-labels-idx1-ubyte.gz', 'r')
buffer_test_y = test_y_gzip.read(n_test)
data_test_y = np.frombuffer(buffer_test_y, dtype=np.uint8)

model = svm.SVC(kernel='rbf', C=100, decision_function_shape='ovr')
model.fit(data_train_X, data_train_y)

y_pred = model.predict(data_test_X)

print("Accuracy: ", accuracy_score(data_test_y, y_pred))

