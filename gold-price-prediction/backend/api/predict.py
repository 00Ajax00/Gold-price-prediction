
import numpy as np
from backend.models.model import load_model, predict_price

def get_prediction():
    model = load_model()
    sample_input = np.array([[1900]])  # Example input
    prediction = predict_price(model, sample_input)
    return {"predicted_price": prediction.tolist()}