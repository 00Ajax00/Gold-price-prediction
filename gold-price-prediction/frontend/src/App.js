
import React, { useState, useEffect } from "react";

function App() {
    const [price, setPrice] = useState(null);

    useEffect(() => {
        fetch("http://localhost:8000/predict")
            .then((res) => res.json())
            .then((data) => setPrice(data.predicted_price));
    }, []);

    return (
        <div>
            <h1>Gold Price Prediction</h1>
            <p>Predicted Price: {price}</p>
        </div>
    );
}

export default App;