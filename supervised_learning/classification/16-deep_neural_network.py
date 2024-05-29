#!/usr/bin/env python3
"""Big boi documentation"""
import numpy as np


class DeepNeuralNetwork:
    """Classdocumentartion"""
    def __init__(self, nx, layers):
        """init documentation"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        