#!/usr/bin/env python3
"""This is documentation"""
import numpy as np


class Neuron:
    """This is documented"""
    def __init__(self, nx):
        """This is also documented"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self._W = np.random.normal(size=(1, nx))
        self._b = 0
        self._A = 0

        def get_W(self):
            """Getter for weight vector"""
            return self.__W

        def get_b(self):
            """Getter for bias"""
            return self.__b

        def get_A(self):
            """Getter for activated output"""
            return self.__A
