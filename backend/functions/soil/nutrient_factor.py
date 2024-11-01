# Ideal levels and weights for different tree types
IDEAL_NUTRIENT_LEVELS = {
    "teak": {"nitrogen": 80, "phosphorus": 40, "potassium": 40, "organic_matter": 30},
    "oak": {"nitrogen": 70, "phosphorus": 35, "potassium": 45, "organic_matter": 25},
    "pine": {"nitrogen": 65, "phosphorus": 30, "potassium": 35, "organic_matter": 20},
    # Add more tree types as needed
}

NUTRIENT_WEIGHTS = {
    "teak": {"nitrogen": 0.4, "phosphorus": 0.2, "potassium": 0.2, "organic_matter": 0.2},
    "oak": {"nitrogen": 0.35, "phosphorus": 0.25, "potassium": 0.2, "organic_matter": 0.2},
    "pine": {"nitrogen": 0.3, "phosphorus": 0.25, "potassium": 0.25, "organic_matter": 0.2},
    # Add more tree types as needed
}

def calculate_nutrient_factor(nitrogen, phosphorus, potassium, organic_matter, tree_type):
    # Check if tree type exists in the dictionaries
    if tree_type.lower() not in IDEAL_NUTRIENT_LEVELS or tree_type.lower() not in NUTRIENT_WEIGHTS:
        raise ValueError(f"Nutrient data for tree type '{tree_type}' is not defined.")

    # Retrieve ideal levels and weights for the specific tree type
    ideal_levels = IDEAL_NUTRIENT_LEVELS[tree_type.lower()]
    weights = NUTRIENT_WEIGHTS[tree_type.lower()]
    
    # Calculate each nutrient factor (capped at 1 if actual > ideal)
    nitrogen_factor = min(nitrogen / ideal_levels["nitrogen"], 1.0)
    phosphorus_factor = min(phosphorus / ideal_levels["phosphorus"], 1.0)
    potassium_factor = min(potassium / ideal_levels["potassium"], 1.0)
    organic_matter_factor = min(organic_matter / ideal_levels["organic_matter"], 1.0)

    # Calculate weighted nutrient factor
    nutrient_factor = (
        (nitrogen_factor * weights["nitrogen"]) +
        (phosphorus_factor * weights["phosphorus"]) +
        (potassium_factor * weights["potassium"]) +
        (organic_matter_factor * weights["organic_matter"])
    )

    return round(nutrient_factor, 2)
