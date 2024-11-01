from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Helper functions for each calculation step
def calculate_vigor(previous_vigor, sunlight_exposure, lambda_):
    Q = np.exp(-0.5 * sunlight_exposure)
    return previous_vigor * (lambda_ * Q) / (lambda_ * Q + (1 - lambda_) * Q)

def normalize_vigor(vigor, min_vigor, max_vigor):
    return (vigor - min_vigor) / (max_vigor - min_vigor)

def calculate_growth_rate(normalized_vigor, global_growth_rate, temperature_adaptation, soil_quality, waterlogging):
    base_growth_rate = (3 * normalized_vigor ** 2 - 2 * normalized_vigor ** 3)
    environmental_adjustment = soil_quality * (1 - waterlogging)
    return base_growth_rate * global_growth_rate * temperature_adaptation * environmental_adjustment

@app.route('/predict-growth', methods=['POST'])
def predict_growth():
    data = request.json
    num_years = int(data.get('numYears', 10))
    plant_type = data.get('plantType', 'teak')
    initial_height = float(data.get('initialHeight', 0.1))
    initial_diameter = float(data.get('initialDiameter', 0.01))
    sunlight_exposure = float(data.get('sunlightExposure', 0.8))
    soil_quality = float(data.get('soilQuality', 0.9))
    waterlogging = float(data.get('waterlogging', 0.1))
    temperature_adaptation = float(data.get('temperatureAdaptation', 0.9))

    # Fetch parameters from user input or defaults from plant_params
    plant_params = get_plant_params(plant_type)
    lambda_ = float(data.get('lambda', plant_params['lambda']))
    min_vigor = float(data.get('minVigor', plant_params['min_vigor']))
    max_vigor = float(data.get('maxVigor', plant_params['max_vigor']))
    global_growth_rate = float(data.get('globalGrowthRate', plant_params['global_growth_rate']))

    # Initialize variables
    height = initial_height
    diameter = initial_diameter
    vigor = min_vigor
    growth_data = []

    for year in range(1, num_years + 1):
        vigor = calculate_vigor(vigor, sunlight_exposure, lambda_)
        normalized_vigor = normalize_vigor(vigor, min_vigor, max_vigor)
        growth_rate = calculate_growth_rate(normalized_vigor, global_growth_rate, temperature_adaptation, soil_quality, waterlogging)

        height += height * growth_rate
        diameter += diameter * 0.8 * growth_rate
        growth_data.append({"year": year, "height": height, "diameter": diameter})

    return jsonify(growth_data)

def get_plant_params(plant_type):
    plant_parameters = {
        "teak": {
            "min_vigor": 0.2,
            "max_vigor": 1.0,
            "lambda": 0.6,
            "global_growth_rate": 1.2,
        },
        "oak": {
            "min_vigor": 0.25,
            "max_vigor": 1.05,
            "lambda": 0.65,
            "global_growth_rate": 1.1,
        },
    }
    return plant_parameters.get(plant_type, plant_parameters["teak"])

if __name__ == "__main__":
    app.run(debug=True)
