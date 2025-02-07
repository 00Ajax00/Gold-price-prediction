import React, { useState } from "react";

function App() {
    const [inputData, setInputData] = useState("");
    const [prediction, setPrediction] = useState(null);

    const handlePredict = async () => {
        const response = await fetch("http://localhost:8000/predict/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify([parseFloat(inputData)]),
        });
        const data = await response.json();
        setPrediction(data.prediction);
    };

    return (
        <div style={{ textAlign: "center", padding: "20px" }}>
            <h2>Gold Price Prediction</h2>
            <input
                type="number"
                value={inputData}
                onChange={(e) => setInputData(e.target.value)}
                placeholder="Enter recent gold price"
            />
            <button onClick={handlePredict}>Predict</button>
            {prediction && <h3>Predicted Price: {prediction[0]}</h3>}
        </div>
    );
}

export default App;
