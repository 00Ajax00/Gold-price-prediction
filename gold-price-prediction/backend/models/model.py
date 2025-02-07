
import numpy as np
import tensorflow as tf

def load_model():
    return tf.keras.models.load_model("backend/models/gold_price_model.h5")

def predict_price(model, input_data):
    return model.predict(input_data)