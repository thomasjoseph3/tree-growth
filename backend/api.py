from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
from backend.functions.soil.soil_quality import calculate_soil_quality


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


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


if __name__ == "__main__":
    app.run(debug=True)
