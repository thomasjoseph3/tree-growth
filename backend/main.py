from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Helper functions
def calculate_vigor(previous_vigor, sunlight_exposure, lambda_):
    Q = np.exp(-0.5 * sunlight_exposure)
    return previous_vigor * (lambda_ * Q) / (lambda_ * Q + (1 - lambda_) * Q)

def calculate_soil_quality(soil_type, pH, tree_type, nutrient_factor=0.8):
    # Base quality scores by soil type
    soil_base_quality = {
        "loamy": 0.9,
        "sandy": 0.5,
        "clay": 0.5,
        "silt": 0.6,
    }

    # Tree preferences and tolerance levels for different species
    tree_preferences = {
        "teak": {
            "preferred_soils": ["loamy", "sandy"],
            "pH_range": (6, 7.5),  # Ideal pH range for teak
            "pH_tolerance": 3,     # Maximum pH deviation tree can tolerate
        },
        # Additional tree types can be added here
    }

    # Fetch the base quality for soil type
    base_quality = soil_base_quality.get(soil_type.lower(), 0.5)

    # Fetch the preferences for the specific tree type
    tree_prefs = tree_preferences.get(tree_type.lower(), {})

    # Check if the soil type is preferred for this tree
    if soil_type.lower() in tree_prefs.get("preferred_soils", []):
        min_pH, max_pH = tree_prefs.get("pH_range", (6, 7.5))
        tolerance = tree_prefs.get("pH_tolerance", 3)

        # Calculate deviation from the ideal pH range only if outside the exact boundaries
        if pH < min_pH:
            pH_deviation = min_pH - pH
        elif pH > max_pH:
            pH_deviation = pH - max_pH
        else:
            pH_deviation = 0  # No penalty for exact boundary values

        # Apply penalty only if there is a deviation
        if pH_deviation == 0:
            penalty = 0
        else:
            # Penalty is based on how far the pH is from ideal, relative to tolerance
            penalty = min(0.5, (pH_deviation / tolerance) ** 2)  # Squared for sharp drop-off

        # Calculate final quality, adjusting for nutrient factor and ensuring minimum quality of 0
        final_quality = max((base_quality - penalty) * nutrient_factor, 0)
        return final_quality

    else:
        # Non-preferred soil significantly reduces quality, adjusted by nutrient factor
        return max((base_quality * 0.5) * nutrient_factor, 0)


def calculate_sunlight_exposure(sunlight_hours, position):
    exposure = sunlight_hours / 12
    if position == 'full shade':
        exposure *= 0.5
    elif position == 'partial shade':
        exposure *= 0.75
    return min(exposure, 1)

def calculate_waterlogging(rainfall, drainage):
    if rainfall == 'high' and drainage == 'poor':
        return 0.9
    elif rainfall == 'moderate' and drainage == 'well-drained':
        return 0.3
    return 0.6

# Flask API Endpoints
@app.route('/calculate_vigor', methods=['POST'])
def vigor_api():
    data = request.json
    previous_vigor = data.get('previousVigor', 0.5)
    sunlight_exposure = data.get('sunlightExposure', 0.8)
    lambda_ = data.get('lambda', 0.6)
    
    vigor = calculate_vigor(previous_vigor, sunlight_exposure, lambda_)
    return jsonify({"vigor": vigor})

# Define the API route
@app.route('/calculate_soil_quality', methods=['POST'])
def soil_quality_api():

    # data = request.json
    # soil_type = data.get('soilType', 'loamy')
    # pH = float(data.get('pH', 6.5))
    # tree_type = data.get('treeType', 'teak')
    data = request.json
    soil_type = data['soilType']
    pH = float(data['pH'])
    tree_type = data['treeType']

    # Calculate soil quality
    soil_quality = calculate_soil_quality(soil_type, pH, tree_type)
    return jsonify({"soil_quality": soil_quality})

@app.route('/calculate_sunlight_exposure', methods=['POST'])
def sunlight_exposure_api():
    data = request.json
    sunlight_hours = data.get('sunlightHours', 8)
    position = data.get('position', 'open field')
    
    exposure = calculate_sunlight_exposure(sunlight_hours, position)
    return jsonify({"sunlight_exposure": exposure})

@app.route('/calculate_waterlogging', methods=['POST'])
def waterlogging_api():
    data = request.json
    rainfall = data.get('rainfall', 'moderate')
    drainage = data.get('drainage', 'well-drained')
    
    waterlogging = calculate_waterlogging(rainfall, drainage)
    return jsonify({"waterlogging": waterlogging})

# Full growth prediction API that combines all factors
@app.route('/predict_growth', methods=['POST'])
def predict_growth():
    data = request.json
    # Example initial parameters
    plant_type = data.get('plantType', 'teak')
    num_years = int(data.get('numYears', 10))
    initial_height = float(data.get('initialHeight', 0.1))
    initial_diameter = float(data.get('initialDiameter', 0.01))
    
    # Retrieve calculated parameters or calculate in place
    soil_quality = calculate_soil_quality(data.get('soilType', 'loamy'), data.get('pH', 6.5))
    sunlight_exposure = calculate_sunlight_exposure(data.get('sunlightHours', 8), data.get('position', 'open field'))
    waterlogging = calculate_waterlogging(data.get('rainfall', 'moderate'), data.get('drainage', 'well-drained'))
    
    # Assuming default temperature adaptation for the example
    temperature_adaptation = 0.9  # Teak-specific example
    
    # Growth calculation with predefined vigor and growth rate logic
    growth_data = []
    height = initial_height
    diameter = initial_diameter
    vigor = 0.5  # Starting vigor for example

    for year in range(1, num_years + 1):
        vigor = calculate_vigor(vigor, sunlight_exposure, 0.6)
        normalized_vigor = (vigor - 0.2) / (1.0 - 0.2)
        base_growth_rate = (3 * normalized_vigor ** 2 - 2 * normalized_vigor ** 3)
        growth_rate = base_growth_rate * 1.2 * temperature_adaptation * soil_quality * (1 - waterlogging)

        height += height * growth_rate
        diameter += diameter * 0.8 * growth_rate

        growth_data.append({"year": year, "height": height, "diameter": diameter})

    return jsonify(growth_data)

if __name__ == "__main__":
    app.run(debug=True)
