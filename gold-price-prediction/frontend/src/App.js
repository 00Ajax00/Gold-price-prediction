import React, { useState } from "react";

function App() {
    const [inputData, setInputData] = useState("");
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handlePredict = async () => {
        if (!inputData) {
            setError("Please enter a valid gold price.");
            return;
        }

        setLoading(true);
        setError(null);
        try {
            const response = await fetch(process.env.REACT_APP_API_URL || "http://localhost:8000/predict/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify([parseFloat(inputData)]),
            });

            if (!response.ok) {
                throw new Error("Failed to fetch prediction.");
            }

            const data = await response.json();
            setPrediction(data.prediction);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
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
            <button onClick={handlePredict} disabled={loading}>
                {loading ? "Predicting..." : "Predict"}
            </button>

            {error && <p style={{ color: "red" }}>{error}</p>}
            {prediction && <h3>Predicted Price: {prediction[0]}</h3>}
        </div>
    );
}

export default App;
