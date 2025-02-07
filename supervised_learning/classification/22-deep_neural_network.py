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

    def __init__(self, nx, layers):
        """DOCUMENTAYUSIN"""
        pass

    def forward_prop(self, X):
        """SIDJIJDFIJDF"""
        pass

    def cost(self, Y, A):
        """DSOJDI(SJD)"""
        pass

    def evaluate(self, X, Y):
        """SODJKDOS"""
        pass

    def gradient_descent(self, Y, cache, alpha=0.05):
        """SODJKDOS"""
        pass

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """SODJKDOS"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
