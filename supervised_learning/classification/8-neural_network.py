#!/usr/bin/env python3
"""DOCUMENTATION"""
import numpy as np


class NeuralNetwork:
    """DOCUMENTATION"""
    def __init__(self, nx, nodes):
        """MORE DOCUMENATION"""
        # Error handling
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.normal(size=(nodes, nx))
        self.b1 = np.zeros((nodes, 1))
        self.A1 = np.zeros((nodes, 1))
        self.W2 = np.random.normal(size=(1, nodes))
        self.b2 = np.zeros((1, 1))
        self.A2 = np.zeros((1, 1))
