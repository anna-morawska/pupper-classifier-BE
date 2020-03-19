import json
import keras
import numpy as np
import tensorflow as tf
import pandas as pd
import tensorflow_hub as hub

IMG_SIZE = 224
BATCH_SIZE = 32
unique_labels = np.unique(np.array(pd.read_csv('labels.csv')["breed"]))
model = tf.keras.models.load_model('17-03-2020-20_48_49-full-image-set.h5', 
                                     custom_objects={"KerasLayer": hub.KerasLayer})


def process_image(uploaded_image, img_size=IMG_SIZE):
    image = tf.image.decode_jpeg(uploaded_image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, size=[img_size, img_size])

    return image

def get_predict_label(prediction_probability):
    return unique_labels[np.argmax(prediction_probability)]


def get_top_10_predictions(prediction_probability):
    top_10_pred_indexes = prediction_probability.argsort()[-10:][::-1]
    top_10_pred_values = prediction_probability[top_10_pred_indexes] * 100
    top_10_pred_labels = unique_labels[top_10_pred_indexes]

    return top_10_pred_values, top_10_pred_labels


def classify_image(uploaded_file):
    data = tf.data.Dataset.from_tensor_slices(tf.constant([uploaded_file]))
    data_batch = data.map(process_image).batch(BATCH_SIZE)
    predictions = model.predict(data_batch)
    
    values, label = get_top_10_predictions(predictions[0])
  
    values =  pd.Series(values)
    labels =  pd.Series(label)

    data = pd.DataFrame({"labels": labels, "values": values}) 
    data = json.loads(data.to_json())
    
    return data
