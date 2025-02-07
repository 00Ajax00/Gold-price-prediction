import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import os
import joblib

MODEL_PATH = "backend/models/gold_price_model.h5"
SCALER_PATH = "backend/models/scaler.pkl"

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

def load_or_train_model(train_data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    train_scaled = scaler.fit_transform(train_data)
    
    if not os.path.exists(MODEL_PATH):
        model = build_model((train_scaled.shape[1], 1))
        model.fit(train_scaled, train_scaled, epochs=50, batch_size=32, verbose=1)
        model.save(MODEL_PATH)
        joblib.dump(scaler, SCALER_PATH)
    else:
        model = tf.keras.models.load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

    return model, scaler

def predict_price(model, scaler, input_data):
    input_scaled = scaler.transform(input_data)
    return model.predict(input_scaled)
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import os
import joblib

MODEL_PATH = "backend/models/gold_price_model.h5"
SCALER_PATH = "backend/models/scaler.pkl"

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

def load_or_train_model(train_data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    train_scaled = scaler.fit_transform(train_data)
    
    if not os.path.exists(MODEL_PATH):
        model = build_model((train_scaled.shape[1], 1))
        model.fit(train_scaled, train_scaled, epochs=50, batch_size=32, verbose=1)
        model.save(MODEL_PATH)
        joblib.dump(scaler, SCALER_PATH)
    else:
        model = tf.keras.models.load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

    return model, scaler

def predict_price(model, scaler, input_data):
    input_scaled = scaler.transform(input_data)
    return model.predict(input_scaled)
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import os
import joblib

MODEL_PATH = "backend/models/gold_price_model.h5"
SCALER_PATH = "backend/models/scaler.pkl"

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

def load_or_train_model(train_data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    train_scaled = scaler.fit_transform(train_data)
    
    if not os.path.exists(MODEL_PATH):
        model = build_model((train_scaled.shape[1], 1))
        model.fit(train_scaled, train_scaled, epochs=50, batch_size=32, verbose=1)
        model.save(MODEL_PATH)
        joblib.dump(scaler, SCALER_PATH)
    else:
        model = tf.keras.models.load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

    return model, scaler

def predict_price(model, scaler, input_data):
    input_scaled = scaler.transform(input_data)
    return model.predict(input_scaled)
