
from fastapi import FastAPI
from backend.api.predict import get_prediction

app = FastAPI()

@app.get("/predict")
def predict():
    return get_prediction()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)