#!/usr/bin/env python3
"""DOCUMENTATION"""
import tensorflow.keras as K


def save_config(network, filename):
    """DONT forget documentation"""
    config = network.to_json()
    with open(filename, 'w') as json_file:
        json_file.write(config)


def load_config(filename):
    """Documentation"""
    with open(filename, "r") as f:
        model = f.read()
    return K.models.model_from_json(model)
