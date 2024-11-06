import React, { useState } from 'react';

const fields = {
    qualityFields: [
        { label: 'Initial Age', name: 'initial_age', type: 'number' },
        { label: 'Initial Height', name: 'initial_height', type: 'number' },
        { label: 'Initial DBH', name: 'initial_dbh', type: 'number' },
        { label: 'Initial Volume', name: 'initial_volume', type: 'number' },
        { label: 'Target Age', name: 'target_age', type: 'number' },
        { label: 'Tree Type', name: 'tree_type', type: 'text' },
        { label: 'Soil Type', name: 'soil_type', type: 'text' },
        { label: 'pH', name: 'pH', type: 'number' },
        { label: 'Nitrogen', name: 'nitrogen', type: 'number' },
        { label: 'Phosphorus', name: 'phosphorus', type: 'number' },
        { label: 'Potassium', name: 'potassium', type: 'number' },
        { label: 'Organic Matter', name: 'organic_matter', type: 'text' },
        { label: 'Min Temperature', name: 'min_temp', type: 'number' },
        { label: 'Max Temperature', name: 'max_temp', type: 'number' },
        { label: 'Temperature', name: 'temp', type: 'number' },
        { label: 'Cold Tolerance', name: 'cold_tolerance', type: 'number' },
        { label: 'Heat Tolerance', name: 'heat_tolerance', type: 'number' },
        { label: 'Annual Rainfall (mm)', name: 'annual_rainfall', type: 'number' },
        { label: 'Drainage Quality', name: 'drainage', type: 'text' }
    ]
};

const Graph = () => {
    const [formData, setFormData] = useState({
        initial_age: '',
        initial_height: '',
        initial_dbh: '',
        initial_volume: '',
        target_age: '',
        tree_type: '',
        soil_type: '',
        pH: '',
        nitrogen: '',
        phosphorus: '',
        potassium: '',
        organic_matter: '',
        min_temp: '',
        max_temp: '',
        temp:'',
        cold_tolerance: '',
        heat_tolerance: '',
        annual_rainfall: '',
        drainage: ''
    });

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
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            
            const result = await response.json();
            console.log('Response from backend:', result);
        } catch (error) {
            console.error('Error sending data to backend:', error);
        }
    };

    const renderFormSection = (title, fields) => (
        <div className='border border-sky-950 w-full p-4 space-y-4'>
            <h1 className='underline text-sm'>{title}</h1>
            {fields.map((field) => (
                <div className='p-1' key={field.name}>
                    <label className='text-sm' htmlFor={field.name}>
                        {field.label}
                    </label>
                    <input
                        type={field.type}
                        name={field.name}
                        id={field.name}
                        value={formData[field.name] || ''}
                        onChange={handleChange}
                        className='border border-gray-300 w-full'
                    />
                </div>
            ))}
        </div>
    );

    return (
        <div className='grid grid-cols-4 gap-4 h-screen overflow-hidden'>
            <div className='col-span-1 p-1 overflow-y-auto'>
                {renderFormSection("Growth Parameters", fields.qualityFields)}
                <button onClick={handleSubmit} className="bg-blue-500 text-white px-4 py-2 rounded mt-4">
                    Submit
                </button>
            </div>
            <div className='col-span-3 p-4 border border-gray-300 flex justify-center items-center'>
                <div className='w-full h-full bg-gray-100 flex justify-center items-center'>
                    <p>Place for chart</p>
                </div>
            </div>
        </div>
    );
};

export default Graph;
