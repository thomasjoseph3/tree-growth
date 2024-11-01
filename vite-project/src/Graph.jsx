import React, { useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";

function GrowthPredictionApp() {
    const [growthData, setGrowthData] = useState([]);
    const [formData, setFormData] = useState({
        plantType: "teak",
        initialHeight: 0.2,  // 20 cm in meters
        initialDiameter: 0.02,  // 2 cm in meters
        numYears: 10,
        sunlightExposure: 0.8,
        soilQuality: 0.9,
        waterlogging: 0.1,
        temperatureAdaptation: 0.9,
        lambda: 0.6,
        minVigor: 0.2,
        maxVigor: 1.0,
        globalGrowthRate: 1.2,
    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: parseFloat(value) || value  // Ensure values are floats where needed
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch("http://localhost:5000/predict-growth", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        });
        const growthData = await response.json();
        setGrowthData(growthData); // Store data for chart visualization
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" name="plantType" value={formData.plantType} onChange={handleInputChange} placeholder="Plant Type" />
                <input type="number" name="initialHeight" value={formData.initialHeight} onChange={handleInputChange} placeholder="Initial Height (m)" step="0.01" />
                <input type="number" name="initialDiameter" value={formData.initialDiameter} onChange={handleInputChange} placeholder="Initial Diameter (m)" step="0.01" />
                <input type="number" name="numYears" value={formData.numYears} onChange={handleInputChange} placeholder="Number of Years" />
                <input type="number" name="sunlightExposure" value={formData.sunlightExposure} onChange={handleInputChange} placeholder="Sunlight Exposure (0-1)" step="0.01" />
                <input type="number" name="soilQuality" value={formData.soilQuality} onChange={handleInputChange} placeholder="Soil Quality (0-1)" step="0.01" />
                <input type="number" name="waterlogging" value={formData.waterlogging} onChange={handleInputChange} placeholder="Waterlogging (0-1)" step="0.01" />
                <input type="number" name="temperatureAdaptation" value={formData.temperatureAdaptation} onChange={handleInputChange} placeholder="Temperature Adaptation (0-1)" step="0.01" />
                <input type="number" name="lambda" value={formData.lambda} onChange={handleInputChange} placeholder="Apical Control Lambda" step="0.01" />
                <input type="number" name="minVigor" value={formData.minVigor} onChange={handleInputChange} placeholder="Minimum Vigor" step="0.01" />
                <input type="number" name="maxVigor" value={formData.maxVigor} onChange={handleInputChange} placeholder="Maximum Vigor" step="0.01" />
                <input type="number" name="globalGrowthRate" value={formData.globalGrowthRate} onChange={handleInputChange} placeholder="Global Growth Rate" step="0.01" />
                <button type="submit">Predict Growth</button>
            </form>

            <LineChart width={600} height={300} data={growthData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="height" stroke="#82ca9d" />
                <Line type="monotone" dataKey="diameter" stroke="#8884d8" />
            </LineChart>
        </div>
    );
}

export default GrowthPredictionApp;
