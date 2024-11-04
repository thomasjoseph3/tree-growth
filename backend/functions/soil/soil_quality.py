import math
from  functions.soil.nutrient_factor import calculate_nutrient_factor

# Soil quality calculation with dynamic nutrient factor
def calculate_soil_quality(soil_type, pH, tree_type, nitrogen, phosphorus, potassium, organic_matter):
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

    # Calculate the nutrient factor dynamically
    nutrient_factor = calculate_nutrient_factor(nitrogen, phosphorus, potassium, organic_matter, tree_type)
    print("Nutrient Factor:", nutrient_factor)

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
            penalty = min(0.5, math.log(1 + (pH_deviation / tolerance)))

        # Calculate final quality, adjusting for nutrient factor and ensuring minimum quality of 0
        final_quality = max((base_quality - penalty) * nutrient_factor, 0)
        return final_quality

    else:
        # Non-preferred soil significantly reduces quality, adjusted by nutrient factor
        return max((base_quality * 0.5) * nutrient_factor, 0)

# # Example usage
# soil_quality = calculate_soil_quality(
#     soil_type="loamy", 
#     pH=6.5, 
#     tree_type="teak", 
#     nitrogen=75, 
#     phosphorus=35, 
#     potassium=40, 
#     organic_matter=28
# )

# print("Soil Quality:", soil_quality)
