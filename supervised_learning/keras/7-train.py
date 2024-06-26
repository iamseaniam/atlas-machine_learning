#!/usr/bin/env python3
"""DOCUmentation"""
import tensorflow.keras as K

def train_model(network, data,
                labels, batch_size,
                epochs, validation_data=None,
                early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True,
                shuffle=False
                ):
    """
    Trains a model using mini-batch gradient descent and includes options for early stopping and learning rate decay.
    """
    callbacks = []

    if early_stopping and validation_data:
        early_stopping_cb = K.callbacks.EarlyStopping(monitor='val_loss',
                                                      patience=patience
                                                      )
        callbacks.append(early_stopping_cb)

    if learning_rate_decay and validation_data:
        def lr_scheduler(epoch, lr):
            return alpha / (1 + decay_rate * epoch)
        lr_decay_cb = K.callbacks.LearningRateScheduler(lr_scheduler,
                                                        verbose=1
                                                        )
    
        callbacks.append(lr_decay_cb)

    history = network.fit(data,
                          labels,
                          batch_size=batch_size,
                          epochs=epochs,
                          validation_data=validation_data,
                          verbose=verbose,
                          shuffle=shuffle,
                          callbacks=callbacks
                          )

    return history