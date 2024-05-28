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

        self.__W = np.random.rand(1, nx)
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
