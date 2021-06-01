#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import tensorflow as tf
tf.keras.backend.clear_session()
import matplotlib.pyplot as plt
import numpy as np

#%%
'''
load image data from fashion_mnist dataset
'''
imgShape = (28, 28)
(raw_train_X, raw_train_y), (raw_test_X, raw_test_y) = tf.keras.datasets.fashion_mnist.load_data()

train_X = raw_train_X / 255
test_X = raw_test_X / 255

test_y = raw_test_y
train_y = np.eye(10)[raw_train_y]

#%%
'''
multi-class classifier using deep neural network
'''
%load_ext tensorboard
import datetime
log_dir = f"./logs/fit/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
tb_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))
model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

optimizer = tf.keras.optimizers.Adam()
model.compile(optimizer=optimizer, metrics=[tf.metrics.categorical_accuracy], loss=tf.losses.categorical_crossentropy)

es = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=20, min_delta=0, restore_best_weights=True)

model.fit(train_X, train_y, validation_split=0.2, epochs=10, callbacks=[es, tb_callback])

test_pred_y = np.argmax(model.predict(test_X), axis=1)

acc = tf.metrics.Accuracy()
acc.reset_state()
acc.update_state(test_y, test_pred_y)
acc.result().numpy()

#%%
'''
multi-class classifier using convolutional neural network
'''
layers = [
        tf.keras.layers.InputLayer(input_shape=imgShape),
        tf.keras.layers.Reshape(list(imgShape)+[1]),
        tf.keras.layers.Conv2D(5, strides=(1, 1), kernel_size=(5, 5)),
        tf.keras.layers.AveragePooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(100, activation=tf.keras.activations.sigmoid, kernel_regularizer=tf.keras.regularizers.L2(0.001)),
        tf.keras.layers.Dense(10, activation=tf.keras.activations.softmax)
    ]

cnn = tf.keras.models.Sequential(layers)

optimizer = tf.keras.optimizers.Adam()
cnn.compile(optimizer=optimizer, metrics=[tf.metrics.CategoricalAccuracy()], loss=tf.losses.categorical_crossentropy)
es = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=20, min_delta=0, restore_best_weights=True)

cnn.fit(train_X, train_y, validation_split=0.2, epochs=100, callbacks=es, batch_size=10000)

test_pred_y = np.argmax(cnn.predict(test_X), axis=1)

acc = tf.metrics.Accuracy()
acc.reset_state()
acc.update_state(test_y, test_pred_y)
acc.result().numpy()
np.savetxt('./y_fashion_mnist_cnn.csv', [test_y, test_pred_y])

#%%
'''
autoencoders using deep neural network
'''
imgShape = (28, 28)
encoder = tf.keras.models.Sequential()
encoder.add(tf.keras.layers.Flatten())
encoder.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))
encoder.add(tf.keras.layers.Dense(64, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))

decoder = tf.keras.models.Sequential()
decoder.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))
decoder.add(tf.keras.layers.Dense(784, activation=tf.nn.relu, kernel_regularizer=tf.keras.regularizers.L2(0.001)))
decoder.add(tf.keras.layers.Reshape(imgShape))

input_tensor = tf.keras.layers.Input(imgShape)
encoder_model = encoder(input_tensor)
decoder_model = decoder(encoder_model)

autoencoder = tf.keras.Model(input_tensor, decoder_model)

optimizer = tf.keras.optimizers.Adamax()
autoencoder.compile(optimizer=optimizer, metrics=[tf.metrics.mean_squared_error], loss=tf.losses.mean_squared_error)

es = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=20, min_delta=0, restore_best_weights=True)

autoencoder.fit(train_X, train_X, validation_split=0.2, epochs=100, callbacks=es)

'''
for intemediate layer output
encoded = tf.keras.Model(inputs = model.input, outputs = model.get_layer('dense_6').output)
'''
#%%
'''
recurrent neural network for NLP
'''
import datetime

from tensorflow.keras.preprocessing import text_dataset_from_directory
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.strings import regex_replace
from tensorflow import keras

path = '/Library/WebServer/Documents/p-EnergyAnalysis/learn_python/datasets/'
train_data = text_dataset_from_directory(f'{path}/imdb/train').unbatch()
test_data = text_dataset_from_directory(f'{path}/imdb/test').unbatch()

def removePunctuationAndHTML(x, y):
    return (regex_replace(x, '<br />', ' '), y)

def filterNegPos(x, y):
    return y!=2

train_data = train_data.filter(filterNegPos)
train_data = train_data.map(removePunctuationAndHTML).batch(500)
test_data = test_data.map(removePunctuationAndHTML).batch(500)

max_tokens = 1000
max_len = 100

vectorize_layer = TextVectorization(max_tokens=max_tokens, output_sequence_length=max_len, output_mode='int')
train_X = train_data.map(lambda x, _: x)
vectorize_layer.adapt(train_X)

model = keras.Sequential()
model.add(vectorize_layer)
model.add(keras.layers.Embedding(max_tokens+1, 128))
model.add(keras.layers.LSTM(64))
model.add(keras.layers.Dense(10, activation=keras.activations.sigmoid))
model.add(keras.layers.Dense(1, activation=keras.activations.sigmoid))
model.compile(optimizer=tf.optimizers.Adam(), loss=tf.losses.BinaryCrossentropy(), metrics=[tf.metrics.BinaryAccuracy()])
model.fit(train_data, epochs=10)

