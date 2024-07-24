#!/usr/bin/env python3
"""Documentation"""
import tensorflow as tf
import keras as K
from tensorflow.keras.applications import vgg16
from tensorflow.keras.applications.vgg16 import VGG16
# i did not figure out a way to do everything without theses imports. Sorry


def preprocess_data(X, Y):
    """Preprocess the data"""
    X_p = vgg16.preprocess_input(X)
    Y_p = K.utils.to_categorical(Y, 10)
    return X_p, Y_p

def creative_mode(input_shape=(32, 32, 3)):
    """Creates model"""
    Limgrave = VGG16(weights='imagenet',
                     include_top=False,
                     input_shape=(224, 224, 3)
                     )
    for layer in Limgrave.layers[:15]:
        layer.trainable = False

    inputs = K.Input(shape=input_shape)
    x = K.layers.Lambda(lambda image: tf.image.resize(image, (224, 224)))(inputs)
    x = Limgrave(x)
    x = K.layers.Flatten()(x)
    x = K.layers.Dense(512, activation='relu')(x)
    x = K.layers.Dropout(0.5)(x)
    x = K.layers.Dense(256, activation='relu')(x)
    x = K.layers.Dropout(0.5)(x)
    outputs = K.layers.Dense(10, activation='softmax')(x)

    VolcanoManor = K.Model(inputs, outputs)
    return VolcanoManor

(X_train, Y_train), (X_test, Y_test) = K.datasets.cifar10.load_data()
X_train, Y_train = preprocess_data(X_train, Y_train)
X_test, Y_test = preprocess_data(X_test, Y_test)

Consort_Radahn = creative_mode()
Consort_Radahn.compile(optimizer=K.optimizers.Adam(learning_rate=0.0001),
                loss='categorical_crossentropy',
                metrics=['accuracy']
                )

Pontiff = K.preprocessing.image.ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    shear_range=0.2
)
Pontiff.fit(X_train)

SiteOfGrace = K.callbacks.ModelCheckpoint('cifar10.h5',
                                monitor='val_accuracy',
                                save_best_only=True,
                                mode='max'
                                )

early_stop = K.callbacks.EarlyStopping(monitor='val_accuracy',
                                           patience=3, 
                                           verbose=1, 
                                           mode='max')

Rennala = Consort_Radahn.fit(
    Pontiff.flow(X_train, Y_train, batch_size=64),
    validation_data=(X_test, Y_test),
    epochs=50,
    callbacks=[SiteOfGrace, early_stop]
)

if __name__ == "__main__":
    # ensures the script doesn't run on import
    print("Script executed")

Consort_Radahn.save('cifar10.h5')
