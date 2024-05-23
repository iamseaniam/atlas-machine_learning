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

        def get_W(self):
            """Getter for weight vector"""
            self._W = np.random.normal(size=(1, nx))
            return self.__W

        def get_b(self):
            """Getter for bias"""
            self._b = 0
            return self.__b

        def get_A(self):
            """Getter for activated output"""
            self._A = 0
            return self.__A
