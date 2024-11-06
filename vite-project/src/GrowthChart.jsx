import React, { useState } from 'react';
import { Line } from 'react-chartjs-2';

const GrowthChart = () => {
    const [formData, setFormData] = useState({});
    const [result, setResult] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/teak-growth', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
            });
            const result = await response.json();
            setResult(result);
        } catch (error) {
            console.error('Error sending data to backend:', error);
        }
    };

    const growthChartData = {
        labels: result?.growth_data.map((data) => data.year),
        datasets: [
            {
                label: 'Height Growth (m)',
                data: result?.growth_data.map((data) => data.height_growth),
                borderColor: 'blue',
                fill: false,
            },
            {
                label: 'DBH Growth (cm)',
                data: result?.growth_data.map((data) => data.dbh_growth),
                borderColor: 'green',
                fill: false,
            },
            {
                label: 'Volume Growth (m³)',
                data: result?.growth_data.map((data) => data.volume_growth),
                borderColor: 'red',
                fill: false,
            },
        ],
    };

    return (
        <div>
            <h2>Enter Growth Parameters</h2>
            <input type="number" name="initial_age" onChange={handleChange} />
            {/* Add other input fields similarly */}
            <button onClick={handleSubmit}>Submit</button>

            {result && (
                <div>
                    <h3>Results</h3>
                    <p>Soil Quality Score: {result.soil_quality}</p>
                    <p>Temperature Adaptation Score: {result.temperature_adaptation}</p>
                    <p>Water Availability Score: {result.water_availability}</p>

                    <table border="1">
                        <thead>
                            <tr>
                                <th>Year</th>
                                <th>Height Growth (m)</th>
                                <th>DBH Growth (cm)</th>
                                <th>Volume Growth (m³)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {result.growth_data.map((yearData) => (
                                <tr key={yearData.year}>
                                    <td>{yearData.year}</td>
                                    <td>{yearData.height_growth}</td>
                                    <td>{yearData.dbh_growth}</td>
                                    <td>{yearData.volume_growth}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>

                    <Line data={growthChartData} />
                </div>
            )}
        </div>
    );
};

export default GrowthChart;
