#!/usr/bin/env python3
"""Example documentation"""
import numpy as np
import tensorflow as tf
import keras as K


class Yolo():
    """Documentation"""

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """Documentation"""
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'rt') as fd:
            self.class_names = fd.read().rstrip('\n').split('\n')
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sigmoid(self, arr):
        """sigmoid activation function"""
        return 1 / (1+np.exp(-1*arr))

    def process_outputs(self, outputs, image_size):
        """Documentation"""
        IH, IW = image_size[0], image_size[1]
        boxes = [output[..., :4] for output in outputs]
        box_confidence, class_probs = [], []
        cornersX, cornersY = [], []

        for output in outputs:
            gridH, gridW, anchors = output.shape[:3]
            cx = np.arange(gridW).reshape(1, gridW)
            cx = np.repeat(cx, gridH, axis=0)
            cy = np.arange(gridW).reshape(1, gridW)
            cy = np.repeat(cy, gridH, axis=0).T

            cornersX.append(
                np.repeat(cx[..., np.newaxis], anchors, axis=2)
                )
            cornersY.append(
                np.repeat(cy[..., np.newaxis], anchors, axis=2)
                )
            box_confidence.append(self.sigmoid(output[..., 4:5]))
            class_probs.append(self.sigmoid(output[..., 5:]))

        inputW = self.model.input.shape[1]
        inputH = self.model.input.shape[2]

        for x, box in enumerate(boxes):
            bx = (
                (self.sigmoid(box[..., 0])+cornersX[x])/outputs[x].shape[1]
                )
            by = (
                (self.sigmoid(box[..., 1])+cornersY[x])/outputs[x].shape[0]
                )
            bw = (
                (np.exp(box[..., 2])*self.anchors[x, :, 0])/inputW
                )
            bh = (
                (np.exp(box[..., 3])*self.anchors[x, :, 1])/inputH
                )

            box[..., 0] = (bx - (bw * 0.5))*IW
            box[..., 1] = (by - (bh * 0.5))*IH
            box[..., 2] = (bx + (bw * 0.5))*IW
            box[..., 3] = (by + (bh * 0.5))*IH

        return (boxes, box_confidence, class_probs)
