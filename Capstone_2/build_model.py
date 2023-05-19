import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, ImageDataGenerator
from tensorflow.keras.applications.xception import Xception, preprocess_input, decode_predictions
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix

# Data Generator
data_gen = {}
for s in ['train', 'validation', 'test']:
  data_gen[s] = ImageDataGenerator(preprocessing_function=preprocess_input, ).flow_from_directory(
      f'./clothing-dataset-small/{s}',
      target_size=(150, 150),
      batch_size=32


# Transfer Learning
base_model=Xception(
    weights='imagenet',
    include_top=False,
    input_shape=(150, 150, 3)
)

base_model.trainable=False

inputs=keras.Input(shape=(150, 150, 3))
base=base_model(inputs, training=False)
pooling=keras.layers.GlobalAveragePooling2D()(base)
outputs=keras.layers.Dense(10, activation='linear')(pooling)
model=keras.Model(inputs, outputs)

# Training
learning_rate=0.01
optimizer=keras.optimizers.Adam(learning_rate=learning_rate)
loss=keras.losses.CategoricalCrossentropy(from_logits=True)
model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
history=model.fit(data_gen['train'], epochs=10,
                    validation_data=data_gen['validation'])

# Save keras model
model.save_weights('clothes-model.h5', save_format='h5')

# Convert Keras to TF-Lite
converter=tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model=converter.convert()
with open('saved_models/clothing-model.tflite', 'wb') as f_out:
  f_out.write(tflite_model)
