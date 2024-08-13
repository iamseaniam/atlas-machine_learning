#!/usr/bin/env python3
"""Example documentation"""
import numpy as np
import tensorflow as tf
import keras as K


class Yolo:
    """YOLO object detection class"""

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """Initialize the YOLO model"""
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'rt') as fd:
            self.class_names = fd.read().rstrip('\n').split('\n')
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sigmoid(self, arr):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-arr))

    def process_outputs(self, outputs, image_size):
        """
        Process model outputs into bounding boxes,
        confidences, and class probabilities
        """
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

            cornersX.append(np.repeat(cx[..., np.newaxis], anchors, axis=2))
            cornersY.append(np.repeat(cy[..., np.newaxis], anchors, axis=2))
            box_confidence.append(self.sigmoid(output[..., 4:5]))
            class_probs.append(self.sigmoid(output[..., 5:]))

        inputW = self.model.input.shape[1]
        inputH = self.model.input.shape[2]

        for x, box in enumerate(boxes):
            bx = (self.sigmoid
                  (box[..., 0]) + cornersX[x]) / outputs[x].shape[1]
            by = (self.sigmoid
                  (box[..., 1]) + cornersY[x]) / outputs[x].shape[0]
            bw = (np.exp(box[..., 2]) * self.anchors[x, :, 0]) / inputW
            bh = (np.exp(box[..., 3]) * self.anchors[x, :, 1]) / inputH

            box[..., 0] = (bx - (bw * 0.5)) * IW
            box[..., 1] = (by - (bh * 0.5)) * IH
            box[..., 2] = (bx + (bw * 0.5)) * IW
            box[..., 3] = (by + (bh * 0.5)) * IH

        return (boxes, box_confidence, class_probs)

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """Filter boxes based on objectness score and class probability"""
        box_scores = [box_conf * class_prob for box_conf,
                      class_prob in zip(box_confidences, box_class_probs)]
        box_classes = [np.argmax
                       (box_score, axis=-1) for box_score in box_scores]
        box_class_scores = [np.max
                            (box_score, axis=-1) for box_score in box_scores]

        filtered_boxes = []
        filtered_classes = []
        filtered_scores = []

        for i in range(len(boxes)):
            filter_mask = box_class_scores[i] >= self.class_t
            filtered_boxes.append(boxes[i][filter_mask])
            filtered_classes.append(box_classes[i][filter_mask])
            filtered_scores.append(box_class_scores[i][filter_mask])

        filtered_boxes = np.concatenate(filtered_boxes, axis=0)
        box_classes = np.concatenate(filtered_classes, axis=0)
        box_scores = np.concatenate(filtered_scores, axis=0)

        return filtered_boxes, box_classes, box_scores

    def non_max_suppression(self, filtered_boxes, box_classes, box_scores):
        """
        Apply Non-Maximum Suppression (NMS) to filter the best bounding boxes
        """
        unique_classes = np.unique(box_classes)
        box_predictions = []
        predicted_box_classes = []
        predicted_box_scores = []

        for cls in unique_classes:
            cls_mask = (box_classes == cls)

            boxes_of_class = filtered_boxes[cls_mask]
            scores_of_class = box_scores[cls_mask]

            selected_indices = tf.image.non_max_suppression(
                boxes_of_class,
                scores_of_class,
                max_output_size=boxes_of_class.shape[0],
                iou_threshold=self.nms_t
            )

            box_predictions.append(tf.gather
                                   (boxes_of_class,
                                    selected_indices).numpy())
            predicted_box_scores.append(tf.gather
                                        (scores_of_class,
                                         selected_indices).numpy())
            predicted_box_classes.append(np.full_like
                                         (tf.gather
                                          (scores_of_class,
                                           selected_indices).numpy(),
                                          cls))

        box_predictions = np.concatenate(box_predictions, axis=0)
        predicted_box_classes = np.concatenate(predicted_box_classes, axis=0)
        predicted_box_scores = np.concatenate(predicted_box_scores, axis=0)

        return box_predictions, predicted_box_classes, predicted_box_scores
