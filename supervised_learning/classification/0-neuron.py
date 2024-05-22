#!/usr/bin/env python3
"""This is documentation"""
import numpy as np


class Neuron:
    """This is documented"""
    def __init__(self,nx):
        """This is also documented"""
        if nx != int():
            TypeError("nx must be an integer")
        if nx >= 1:
            ValueError("nx must be a positive integer")
