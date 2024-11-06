SOIL_RETENTION = {
    "loamy": 0.85,
    "sandy": 0.4,
    "clay": 0.75,
    "laterite": 0.6,        # Found in tropical regions, moderate retention
    "peaty": 0.9,           # High organic content, retains significant moisture
    "black cotton": 0.7,    # Expansive soil, retains moisture moderately well
    "alluvial": 0.8         # Fertile, found in river valleys, moderate to high retention
}

# Define drainage retention factors
DRAINAGE_RETENTION = {
    "well_drained": 0.9,
    "moderately_drained": 0.7,
    "poorly_drained": 0.5
}

# Define optimal water range for different tree types
WATER_RANGE = {
    "teak": (1200, 2500),   # mm, example optimal range for teak
    "pine": (700, 1500),    # Typical optimal range for pine
    "eucalyptus": (800, 1800)  # Typical optimal range for eucalyptus
}

def calculate_water_availability(annual_rainfall, soil_type, drainage, tree_type="teak"):
    """
    Calculate normalized water availability based on rainfall, soil type, drainage quality, and tree-specific requirements.
    
    Parameters:
    - annual_rainfall (float): Total annual rainfall in mm.
    - soil_type (str): Type of soil ("loamy", "sandy", "clay").
    - drainage (str): Drainage quality ("well_drained", "moderately_drained", "poorly_drained").
    - tree_type (str): Type of tree (default is "teak").
    
    Returns:
    - float: Normalized water availability (0 to 1), with penalty decay applied if outside optimal range.
    """
    
    # Get soil retention factor
    soil_retention_factor = SOIL_RETENTION.get(soil_type.lower(), 0.5)  # Default to 0.5 if soil type is unknown
    
    # Get drainage retention factor
    drainage_retention_factor = DRAINAGE_RETENTION.get(drainage.lower(), 0.7)  # Default to 0.7 if drainage is unknown
    
    # Calculate Effective Water Availability (EWA) in mm
    ewa = annual_rainfall * soil_retention_factor * drainage_retention_factor
    
    # Get the optimal water range for the specified tree type
    optimal_water_min, optimal_water_max = WATER_RANGE.get(tree_type.lower(), (1200, 2500))
    
    # Normalize water availability to a range of 0 to 1
    if ewa < optimal_water_min:
        # Apply penalty decay for insufficient water
        normalized_water_availability = (ewa / optimal_water_min) ** 0.5  # Square root decay for low water
    elif ewa > optimal_water_max:
        # Apply penalty decay for excess water
        normalized_water_availability = (optimal_water_max / ewa) ** 0.5  # Square root decay for excess water
    else:
        # Within optimal range, scale linearly between min and max
        normalized_water_availability = (ewa - optimal_water_min) / (optimal_water_max - optimal_water_min)
    
    # Ensure the normalized value is between 0 and 1
    return round(min(max(normalized_water_availability, 0), 1), 2)
