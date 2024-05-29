#!/usr/bin/env python3
"""Big boi documentation"""
import numpy as np


class DeepNeuralNetwork:
    """classification."""
    def __init__(self, nx, layers):
        """deep neural network."""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        if not all(isinstance(x, int) and x > 0 for x in layers):
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        #for l in range(1, self.L + 1):
            #layer_size = layers[l - 1]
            #prev_layer_size = nx if l == 1 else layers[l - 2]
            #self.weights[f'W{l}'] = (np.random.randn(layer_size, prev_layer_size) *
            #                        np.sqrt(2 / prev_layer_size))
            #self.weights[f'b{l}'] = np.zeros((layer_size, 1))
