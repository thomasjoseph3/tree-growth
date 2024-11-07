from flask import Flask, request, jsonify
from flask_cors import CORS
from functions.trees_spec import TREE_PROFILES
from functions.soil.soil_quality import calculate_soil_quality
from functions.temperature.tempreature_score_with_tolerance import calculate_temperature_adaptation
from functions.water.water_availability import calculate_water_availability
from tree_calc.simulate_tree import simulate_tree_growth
from area_growth_calc.calculate_growth import area_growth_calculation
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/tree-growth', methods=['POST'])
def teak_growth():
    data = request.get_json()
    try:
        initial_age = float(data.get('initial_age'))
        initial_height = float(data.get('initial_height'))
        initial_dbh = float(data.get('initial_dbh'))
        initial_volume = float(data.get('initial_volume'))
        target_age = int(data.get('target_age'))
        tree_type=data.get('tree_type')

        soil_quality = calculate_soil_quality(
            soil_type=data.get('soil_type'),
            pH=float(data.get('pH')),
            tree_type=data.get('tree_type'),
            nitrogen=float(data.get('nitrogen')),
            phosphorus=float(data.get('phosphorus')),
            potassium=float(data.get('potassium')),
            organic_matter=float(data.get('organic_matter'))
        )

        temperature_adaptation = calculate_temperature_adaptation(
            float(data.get('temp')),
            (float(data.get('min_temp')), float(data.get('max_temp'))),
            float(data.get('cold_tolerance')),
            float(data.get('heat_tolerance'))
        )

        water_availability = calculate_water_availability(
            float(data.get('annual_rainfall')),
            data.get('soil_type'),
            data.get('drainage')
        )

        growth_result = simulate_tree_growth(
            initial_age=initial_age,
            initial_height=initial_height,
            initial_dbh=initial_dbh,
            initial_volume=initial_volume,
            target_age=target_age,
            tree_profile=TREE_PROFILES[tree_type],
            soil_quality=soil_quality,
            temperature_adaptation=temperature_adaptation,
            water_availability=water_availability
        )

        return jsonify(growth_result)
    
    except (TypeError, ValueError, KeyError) as e:
        return jsonify({"error": "Invalid input data format or missing data", "message": str(e)}), 400

@app.route('/api/area-growth', methods=['POST'])
def area_growth():
    data = request.get_json()

    try:
        # Get parameters from the request
        result = area_growth_calculation(
            area_acres=float(data.get('area_acres')),
            tree_density_per_acre=int(data.get('tree_density_per_acre')),
            initial_age=float(data.get('initial_age')),
            initial_height=float(data.get('initial_height')),
            initial_dbh=float(data.get('initial_dbh')),
            initial_volume=float(data.get('initial_volume')),
            target_age=int(data.get('target_age')),
            tree_type=data.get('tree_type'),
            soil_type=data.get('soil_type'),
            pH=float(data.get('pH')),
            nitrogen=float(data.get('nitrogen')),
            phosphorus=float(data.get('phosphorus')),
            potassium=float(data.get('potassium')),
            organic_matter=float(data.get('organic_matter')),
            temp=float(data.get('temp')),
            min_temp=float(data.get('min_temp')),
            max_temp=float(data.get('max_temp')),
            cold_tolerance=float(data.get('cold_tolerance')),
            heat_tolerance=float(data.get('heat_tolerance')),
            annual_rainfall=float(data.get('annual_rainfall')),
            drainage=data.get('drainage')
        )

        return jsonify(result)

    except (TypeError, ValueError, KeyError) as e:
        return jsonify({"error": "Invalid input data format or missing data", "message": str(e)}), 400
if __name__ == '__main__':
    app.run(debug=True)
