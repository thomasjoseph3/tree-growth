import math
from functions.soil.nutrient_factor import calculate_nutrient_factor
from functions.teak.growth import calculate_growth_rate, calculate_annual_height_growth
from functions.teak.teak import TEAK_PROFILES
from functions.soil.soil_quality import calculate_soil_quality
from functions.temperature.tempreature_score_with_tolerance import calculate_temperature_adaptation
from functions.water.water_availability import calculate_water_availability

# Assuming TREE_PROFILES and environment factor calculation functions are defined as before

def calculate_teak_height_growth(time_period_years, initial_height, base_height_growth_rate,
                                 soil_type, pH, tree_type, nitrogen, phosphorus, potassium, organic_matter,
                                 annual_rainfall, drainage, average_temp, optimal_temp_range, cold_tolerance, heat_tolerance):
    
    # Get species-specific parameters
    tree_profile = TEAK_PROFILES.get(tree_type.lower())
    if not tree_profile:
        raise ValueError(f"No growth profile found for tree type '{tree_type}'")

    growth_phases = tree_profile["growth_phases"]
    max_height = tree_profile["max_height"]

    # Step 1: Calculate environmental factors and the environmental growth factor
    soil_quality = calculate_soil_quality(soil_type, pH, tree_type, nitrogen, phosphorus, potassium, organic_matter)
    temperature_adaptation = calculate_temperature_adaptation(average_temp, optimal_temp_range, cold_tolerance, heat_tolerance)
    water_availability = calculate_water_availability(annual_rainfall, soil_type, drainage)

    # Calculate environmental growth factor
    environmental_growth_factor = calculate_growth_rate(soil_quality, temperature_adaptation, water_availability)
    
    # Initialize current height
    current_height = initial_height
    
    # Step 2: Loop through each year in the time period to calculate height growth
    for year in range(time_period_years):
        # Determine phase multiplier based on age
        phase_multiplier = 1.0
        for (start, end, multiplier) in growth_phases:
            if start <= year < end:
                phase_multiplier = multiplier
                break

        # Adjust growth rate with environmental growth factor and phase multiplier
        adjusted_growth_rate = base_height_growth_rate * environmental_growth_factor * phase_multiplier

        # Calculate height growth for this year
        height_increase = min(calculate_annual_height_growth(adjusted_growth_rate, current_height), max_height - current_height)
        
        # Update current height
        current_height += height_increase

    return {
        "height_increase": round(current_height - initial_height, 2),
        "final_height": round(current_height, 2)
    }

# Example usage with sample data
time_period_years = 2
initial_height = 1.0              # Initial height in meters
base_height_growth_rate = 1.2      # Base growth rate provided by the user for teak under ideal conditions (meters per year)

# Environmental inputs
soil_type = "loamy"
pH = 6.5
tree_type = "teak"
nitrogen = 75
phosphorus = 35
potassium = 40
organic_matter = 28
annual_rainfall = 1200            # Annual rainfall in mm
drainage = "moderately_drained"
average_temp = 25                 # Average annual temperature in °C
optimal_temp_range = (20, 30)     # Optimal temperature range for teak in °C
cold_tolerance = 15               # Cold tolerance in °C
heat_tolerance = 38               # Heat tolerance in °C

# Calculate height growth over the specified period
height_growth_result = calculate_teak_height_growth(
    time_period_years, initial_height, base_height_growth_rate,
    soil_type, pH, tree_type, nitrogen, phosphorus, potassium, organic_matter,
    annual_rainfall, drainage, average_temp, optimal_temp_range, cold_tolerance, heat_tolerance
)

print("Height Growth Result over", time_period_years, "years:", height_growth_result)
