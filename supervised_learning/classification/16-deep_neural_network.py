#!/usr/bin/env python3
"""Big boi documentation"""
import numpy as np


class DeepNeuralNetwork():
    """binary classification."""
    def __init__(self, nx, layers):
        """layers like a cake"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')
        elif type(layers) is not list or len(layers) == 0:
            raise TypeError('layers must be a list of positive integers')
        else:
            self.__L = len(layers)
            self.__cache = {}
            self.__weights = {}
            prev = nx
            for i in range(len(layers)):
                if type(layers[i]) is not int or layers[i] < 1:
                    raise TypeError(
                        'layers must be a list of positive integers')
                w = np.random.randn(layers[i], prev) * np.sqrt(2/prev)
                prev = layers[i]
                self.weights['W{}'.format(i + 1)] = w
                dim = len(self.weights['W{}'.format(i + 1)])
                self.weights['b{}'.format(i + 1)] = np.zeros((dim, 1))

    @property
    def L(self):
        """getter for L"""
        return self.__L

    @property
    def cache(self):
        """getter for cache"""
        return self.__cache

    @property
    def weights(self):
        """getter for weights"""
        return self.__weights
