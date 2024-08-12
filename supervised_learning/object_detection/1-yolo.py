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

    def process_outputs(self, outputs, image_size):
        image_height, image_width = image_size
        boxes = []
        box_confidences = []
        box_class_probs = []
        
        for output in outputs:
            grid_height, grid_width, anchor_boxes = output.shape[:3]
            
            boxes.append(np.zeros((grid_height, grid_width, anchor_boxes, 4)))
            box_confidences.append(np.zeros((grid_height, grid_width, anchor_boxes, 1)))
            box_class_probs.append(np.zeros((grid_height, grid_width, anchor_boxes, self.classes)))
            
            for i in range(grid_height):
                for j in range(grid_width):
                    for k in range(anchor_boxes):
                        tx, ty, tw, th = output[i, j, k, :4]
                        bx = (1 / (1 + np.exp(-tx)) + j) / grid_width
                        by = (1 / (1 + np.exp(-ty)) + i) / grid_height
                        bw = np.exp(tw) / grid_width
                        bh = np.exp(th) / grid_height
                        
                        x1 = (bx - bw / 2) * image_width
                        y1 = (by - bh / 2) * image_height
                        x2 = (bx + bw / 2) * image_width
                        y2 = (by + bh / 2) * image_height
                        
                        boxes[-1][i, j, k] = [x1, y1, x2, y2]
                        
                        box_confidence = 1 / (1 + np.exp(-output[i, j, k, 4]))
                        box_confidences[-1][i, j, k, 0] = box_confidence
                        
                        class_probs = 1 / (1 + np.exp(-output[i, j, k, 5:]))
                        box_class_probs[-1][i, j, k, :] = class_probs
        
        return (boxes, box_confidences, box_class_probs)
