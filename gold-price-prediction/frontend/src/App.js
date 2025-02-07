// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const App = () => {
  const [data, setData] = useState([]);
  const [price, setPrice] = useState(null);

  const fetchPrediction = async () => {
    const res = await axios.get('http://localhost:8000/predict?open=1900&high=1950&low=1880');
    setPrice(res.data.predicted_price);
    setData([...data, res.data.predicted_price]);
  };

  return (
    <div>
      <h1>Gold Price Prediction</h1>
      <button onClick={fetchPrediction}>Predict Price</button>
      <h2>Predicted Price: ${price}</h2>
      <Line data={{ labels: data.map((_, i) => i), datasets: [{ data, label: 'Gold Price', borderColor: 'gold' }] }} />
    </div>
  );
};

export default App;
