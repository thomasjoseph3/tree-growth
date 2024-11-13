import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from flask_cors import CORS
from TreeSimulation import TreeSimulation
from tree_spec import TREE_PROFILES
from SoilQuality import SoilQuality
from TemperatureAdaptation import TemperatureAdaptation
from WaterAvailability import WaterAvailability
from CompetitionIndex import CompetitionIndex
from Tree import Tree

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/tree-growth', methods=['POST'])
def tree_growth():
    data = request.get_json()
    try:
        initial_age = float(data.get('initial_age'))
        initial_height = float(data.get('initial_height'))
        initial_dbh = float(data.get('initial_dbh'))
        initial_volume = float(data.get('initial_volume'))
        target_age = int(data.get('target_age'))
        tree_type = data.get('tree_type')
        tree_spacing = float(data.get('tree_spacing'))

        # Retrieve the tree profile
        tree_profile = TREE_PROFILES[tree_type]
        tree = Tree(tree_type, tree_profile)

        # Initialize factors
        soil_quality = SoilQuality(
            soil_type=data.get('soil_type'),
            pH=float(data.get('pH')),
            nitrogen=float(data.get('nitrogen')),
            phosphorus=float(data.get('phosphorus')),
            potassium=float(data.get('potassium')),
            organic_matter=float(data.get('organic_matter'))
        ).calculate_soil_quality(tree)

        temperature_adaptation = TemperatureAdaptation(
            average_temp=float(data.get('temp')),
            tree=tree
        ).calculate()

        water_availability = WaterAvailability(
            annual_rainfall=float(data.get('annual_rainfall')),
            soil_type=data.get('soil_type'),
            drainage=data.get('drainage'),
            tree=tree
        ).calculate()

        competition_index = CompetitionIndex(
            tree_spacing=tree_spacing,
            influence_radius=10,
            dbh=initial_dbh,
            crown_diameter=None
        )

        # Run simulation
        simulation = TreeSimulation(
            tree=tree,
            soil_quality=soil_quality,
            water_availability=water_availability,
            temperature_adaptation=temperature_adaptation,
            competition_index=competition_index
        )

        growth_result = simulation.simulate_growth(
            initial_age=initial_age,
            initial_height=initial_height,
            initial_dbh=initial_dbh,
            initial_volume=initial_volume,
            target_age=target_age,
            tree_spacing=tree_spacing,
            use_competition=True
        )

        return jsonify(growth_result)
    
    except (TypeError, ValueError, KeyError) as e:
        return jsonify({"error": "Invalid input data format or missing data", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
