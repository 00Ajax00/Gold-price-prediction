from fastapi import FastAPI, HTTPException
import numpy as np
from backend.models.model import load_or_train_model, predict_price

app = FastAPI()

# Load Model
model, scaler = load_or_train_model(np.random.rand(100, 1))  # Dummy training

@app.post("/predict/")
async def predict(input_data: list):
    try:
        input_array = np.array(input_data).reshape(-1, 1)
        prediction = predict_price(model, scaler, input_array)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
