from fastapi import FastAPI, HTTPException
import numpy as np
import logging
from backend.models.model import load_model, predict_price

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained model and scaler
try:
    model, scaler = load_model()
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model, scaler = None, None  # Prevent crashes

@app.post("/predict/")
async def predict(input_data: list):
    try:
        if not isinstance(input_data, list) or not all(isinstance(x, (int, float)) for x in input_data):
            raise HTTPException(status_code=400, detail="Invalid input format. Must be a list of numbers.")
        
        input_array = np.array(input_data).reshape(-1, 1)
        prediction = predict_price(model, scaler, input_array)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
