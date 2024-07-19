#!/usr/bin/env python3
"""DOCUMENTATIOn"""
import tensorflow as tf
import keras as K
import numpy as np
import matplotlib.pyplot as plt
# Notes:
# Use 'Lambda' layer to resize imagies from 32x32 to 224x224. seems like a lot of inputs
# Use a pre-trained model? ('ResNet50') with the 'include_top' para set to false to xclud top class layer
# Freeze pre-trained layers to prevent them from being updated duing training


def preprocess_data(X, Y):
    """Example from website
    function that pre0processes the CIFAR10 dataset as per
    densenet model requirements for input images
    labels are one-hot encoded
    """
    X = K.applications.densenet.preprocess_input(X)
    Y = K.utils.to_categorical(Y)

    return X, Y


# LOAD THE Cifar10 dataset, 50,000 training images
# and  10,000 test images (here used as validation data)
(x_train, y_train), (x_test, y_test) = K.datasets.cifar10.load_data()
# preprocess the data using the application's preprocess_input 
# method and conver the labels to one-hot encodings
x_train, y_train = preprocess_data(x_train, y_train)

# weights are initialized as per the he et al. method 
initializer = K.initializers.he_normal()
input_tensor = K.Input(shape=(32, 32, 3))

# resize images to the image size upon which the network was pre-trained
resized_images = K.layers.Lambda(lambda image: tf.image.resize(image, (224, 224)))(input_tensor)

model = K.applications.DenseNet201(include_top=False,
                                   weights='imagenet',
                                   input_tensor=resized_images,
                                   input_shape=(224, 224, 3),
                                   pooling='max',
                                   classes=1000)

# make the weights and biases of the base model non-trainable
# by "freezing" each layer of the DenseNet202 network

for layer in model.layers:
    layer.trainable = False

output = model.layers[-1].output

# reshape the output feature map of the base model before
# passing the data on to the dense layers of the classifier head
flatten = K.layers.Flatten()
output = flatten(output)

layer_256 = K.layers.Dense(units=256,
                           activation='elu',
                           kernel_initializer=initializer,
                           kernel_regularizer=K.regularizers.l2())
output = layer_256(output)
dropout = K.layers.Dropout(0.5)
output = dropout(output)
softmax = K.layers.Dense(units=10,
                         activation='softmax',
                         kernel_initializer=initializer,
                         kernel_regularizer=K.regularizers.l2())
softmax = softmax(output)


# if __name__ == "__main__":