#!/usr/bin/env python3
"""This is documentation"""
import numpy as np


class Neuron:
    """dOCUmented muffin man"""
    def __init__(self, nx):
        """ Initialize the neuron with nx input features. """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ Getter for the weight vector __W. """
        return self.__W

    @property
    def b(self):
        """ Getter for the bias __b. """
        return self.__b

    @property
    def A(self):
        """ Getter for the activated output __A. """
        return self.__A

    def forward_prop(self, X):
        """Calculate the forward propagation of the neuron."""
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """DOCumentation"""
        m = Y.shape[1]
        cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """Evaluate the neuron’s predictions."""
        A = self.forward_prop(X)
        predictions = (A >= 0.5).astype(int)
        cost = self.cost(Y, A)
        return predictions, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Documentation for sizzles"""
        m = X.shape[1]
        dZ = A - Y
        dW = np.dot(dZ, X.T) / m
        db = np.sum(dZ) / m

        self.__W -= alpha * dW
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """DOCUMENTATIONSJNDS"""
        if not isinstance(iterations, int):
            raise TypeError ("iterations must be an integer")
        if iterations < 0:
            raise TypeError("iterations must be a positive integer")

        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise TypeError("alpha must be positive")

        for iterations in range(iterations):
            A = self.forward_prop(X)
            dZ = A - Y
            dW = self.gradient_descent(dZ, X)
            db = self.gradient_descent(dZ)

            self.__W = self.__W - (alpha * dW)
            self.__b = self.__b - (alpha * db)
