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

    def sigmoid(self, x):
        """Compute sigmoid function"""
        return 1 / (1 + np.exp(-x))

    def process_outputs(self, outputs, image_size):
        """
        Process the model outputs to get bounding boxes, box confidences, and class probabilities.
        """
        boxes = []
        box_confidences = []
        box_class_probs = []

        image_height, image_width = image_size

        for output in outputs:
            grid_height, grid_width, anchor_boxes = output.shape[:3]
            box_xy = self.sigmoid(output[..., :2])
            box_wh = np.exp(output[..., 2:4]) * self.anchors
            box_confidence = self.sigmoid(output[..., 4:5])
            box_class_prob = self.sigmoid(output[..., 5:])

            col = np.tile(np.arange(0, grid_width).reshape(-1, 1, 1), (1, grid_height, anchor_boxes))
            row = np.tile(np.arange(0, grid_height).reshape(1, -1, 1), (grid_width, 1, anchor_boxes))

            box_xy += np.stack([col, row], axis=-1)
            box_xy /= [grid_width, grid_height]

            box_wh /= [self.model.input.shape[1].value, self.model.input.shape[2].value]  # Normalize wh values

            box_xy -= (box_wh / 2)
            box_xy = box_xy * [image_width, image_height]
            box_wh = box_wh * [image_width, image_height]

            box = np.concatenate([box_xy, box_xy + box_wh], axis=-1)

            boxes.append(box)
            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

        return boxes, box_confidences, box_class_probs