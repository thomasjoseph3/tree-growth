# Define soil retention factors for different soil types
SOIL_RETENTION = {
    "loamy": 0.85,
    "sandy": 0.4,
    "clay": 0.75
}

# Define drainage retention factors
DRAINAGE_RETENTION = {
    "well_drained": 0.9,
    "moderately_drained": 0.7,
    "poorly_drained": 0.5
}

def calculate_water_availability(annual_rainfall, soil_type, drainage):
    """
    Calculate effective water availability based on rainfall, soil type, and drainage quality.
    
    Parameters:
    - annual_rainfall (float): Total annual rainfall in mm.
    - soil_type (str): Type of soil ("loamy", "sandy", "clay").
    - drainage (str): Drainage quality ("well_drained", "moderately_drained", "poorly_drained").
    
    Returns:
    - float: Effective water availability in mm.
    """
    
    # Get soil retention factor
    soil_retention_factor = SOIL_RETENTION.get(soil_type.lower(), 0.5)  # Default to 0.5 if soil type is unknown
    
    # Get drainage retention factor
    drainage_retention_factor = DRAINAGE_RETENTION.get(drainage.lower(), 0.7)  # Default to 0.7 if drainage is unknown
    
    # Calculate Effective Water Availability
    ewa = annual_rainfall * soil_retention_factor * drainage_retention_factor
    
    return round(ewa, 2)

# # Example usage
# annual_rainfall = 1200  # mm, example annual rainfall
# soil_type = "loamy"
# drainage = "moderately_drained"

# water_availability = calculate_water_availability(annual_rainfall, soil_type, drainage)
# print("Water Availability:", water_availability, "mm")
