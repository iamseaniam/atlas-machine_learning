#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow.keras as K


def save_weights(network, filename, save_format='keras'):
    """DOCumentation"""
    network.save_weights(filename, save_format=save_format)


def load_weights(network, filename):
    """Documentation"""
    network.load_weights(filename)
