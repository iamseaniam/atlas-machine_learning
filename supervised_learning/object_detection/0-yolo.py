#!/usr/bin/env python3
"""Example documentation"""
import numpy as np
import tensorflow as tf


class Yolo:
    """The YOLOv3 Class documentation"""
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """Example documentation"""
        self.model = tf.keras.models.load_model(model_path)
        
        with open(classes_path, 'r') as file:
            self.class_names = [line.strip() for line in file.readlines()]
        
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors
