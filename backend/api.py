from flask import Flask, request, jsonify
from flask_cors import CORS
import math
from functions.teak.growth import calculate_growth_rate, calculate_annual_height_growth
from functions.soil.soil_quality import calculate_soil_quality
from functions.temperature.tempreature_score_with_tolerance import calculate_temperature_adaptation
from functions.water.water_availability import calculate_water_availability
from functions.trees_spec import TREE_PROFILES
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

def calculate_collar_diameter(dbh):
    """Calculate collar diameter from DBH using the regression equation."""
    return 0.8692 + 1.1 * dbh  # DBH in cm, output also in cm

def simulate_teak_growth(
    initial_age, initial_height, initial_dbh, initial_volume, target_age, teak_profile,
    soil_quality, temperature_adaptation, water_availability
):  
    print(initial_age,initial_dbh,initial_height,initial_volume,target_age,teak_profile,soil_quality,temperature_adaptation,water_availability)

    current_age = initial_age
    current_height = initial_height
    current_dbh = initial_dbh
    current_volume = initial_volume

    # Calculate the combined growth factor
    combined_growth_factor = min(soil_quality, temperature_adaptation, water_availability)
    print(f"soilquality:{soil_quality}")
    print(f"temperature_adaptation:{temperature_adaptation}")
    print(f"water_availability:{water_availability}")
    print(f"Combined Growth Factor: {combined_growth_factor}") 
    
    while current_age < target_age:
        # Determine the current growth phase
        for phase in teak_profile["growth_phases"]:
            if phase["start_age"] <= current_age < phase["end_age"]:
                # Apply growth factor to each growth rate
                height_growth_rate = (phase["height_growth"] / 1000) * combined_growth_factor  # meters
                dbh_growth_rate = phase["dbh_growth"] * combined_growth_factor  # cm/year
                volume_growth_rate = phase["volume_growth"] * combined_growth_factor  # m³/year
                break

        # Incrementally add growth each year, limited by max values
        new_height = min(height_growth_rate, teak_profile["max_values"]["max_height"] - current_height)
        current_height += new_height

        max_dbh = teak_profile["max_values"]["max_canopy_diameter"] * 10  # Max DBH in cm
        new_dbh = min(dbh_growth_rate, max_dbh - current_dbh)
        current_dbh += new_dbh

        new_volume = min(volume_growth_rate, teak_profile["max_values"]["max_biomass"] - current_volume)
        current_volume += new_volume

        # Calculate collar diameter from DBH
        collar_diameter = calculate_collar_diameter(current_dbh)

        # Print step-by-step calculations for each year
        print(f"Year {round(current_age, 2)}:")
        print(f"  Combined Growth Factor: {combined_growth_factor}")
        print(f"  Adjusted Growth Rates - Height: {height_growth_rate * 1000} mm/year, DBH: {dbh_growth_rate} mm/year, Volume: {volume_growth_rate} m³/year")
        print(f"  Updated Values - Height: {round(current_height, 4)} m, DBH: {round(current_dbh, 4)} cm, Volume: {round(current_volume, 4)} m³")
        print(f"  Calculated Collar Diameter: {round(collar_diameter, 2)} cm\n")

        # Increment age by 1 year
        current_age += 1

    return {
        "final_height": round(current_height, 2),
        "final_dbh": round(current_dbh, 2),
        "final_volume": round(current_volume, 2),
        "final_collar_diameter": round(collar_diameter, 2)
    }


@app.route('/api/teak-growth', methods=['POST'])
def teak_growth():
    data = request.get_json()

    try:
        # Parse and convert incoming data to the correct types
        initial_age = float(data.get('initial_age'))
        initial_height = float(data.get('initial_height'))
        initial_dbh = float(data.get('initial_dbh'))
        initial_volume = float(data.get('initial_volume'))
        target_age = int(data.get('target_age'))
        
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

        growth_result = simulate_teak_growth(
            initial_age=initial_age,
            initial_height=initial_height,
            initial_dbh=initial_dbh,
            initial_volume=initial_volume,
            target_age=target_age,
            teak_profile=TREE_PROFILES["teak"],
            soil_quality=soil_quality,
            temperature_adaptation=temperature_adaptation,
            water_availability=water_availability
        )

        return jsonify(growth_result)
    
    except (TypeError, ValueError, KeyError) as e:
        return jsonify({"error": "Invalid input data format or missing data", "message": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
