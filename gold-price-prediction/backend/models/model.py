import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import os
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define paths with environment variable fallback
MODEL_PATH = os.getenv("MODEL_PATH", "backend/models/gold_price_model.h5")
SCALER_PATH = os.getenv("SCALER_PATH", "backend/models/scaler.pkl")

def build_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model

def load_model():
    """Loads a trained model and scaler, or raises an error if missing."""
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("Model or Scaler not found. Please train the model first.")

    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    logger.info("Model and scaler loaded successfully.")
    return model, scaler

def train_and_save_model(train_data):
    """Trains and saves a new model and scaler."""
    try:
        scaler = MinMaxScaler(feature_range=(0, 1))
        train_scaled = scaler.fit_transform(train_data)

        model = build_model((train_scaled.shape[1], 1))
        model.fit(train_scaled, train_scaled, epochs=50, batch_size=32, verbose=1)

        model.save(MODEL_PATH)
        joblib.dump(scaler, SCALER_PATH)
        logger.info("Model and scaler saved successfully.")

    except Exception as e:
        logger.error(f"Training failed: {e}")

def predict_price(model, scaler, input_data):
    """Makes a prediction given input data."""
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return scaler.inverse_transform(prediction)
