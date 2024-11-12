from functions.competition.competition_index import calculate_uniform_competition_index

def calculate_collar_diameter(dbh):
    return 0.8692 + 1.1 * dbh  # DBH in cm, output also in cm

import math

def calculate_crown_size(dbh, height, tree_type):
    """
    Calculate the crown size (diameter and area) for a single tree based on DBH and height.
    
    Parameters:
    - dbh (float): Diameter at Breast Height in cm.
    - height (float): Height of the tree in meters.
    - tree_type (str): Type of the tree species ("teak", "pine", etc.)
    
    Returns:
    - dict: Contains 'crown_diameter' (in meters) and 'crown_area' (in square meters).
    """
    # Define species-specific empirical constants for crown calculation
    species_constants = {
        "teak": {"a": 1.1, "b": 0.8, "c": 0.6},  # Example constants
        "pine": {"a": 0.9, "b": 0.75, "c": 0.5}
    }
    
    # Retrieve constants for the specific tree type
    if tree_type.lower() in species_constants:
        a = species_constants[tree_type.lower()]["a"]
        b = species_constants[tree_type.lower()]["b"]
        c = species_constants[tree_type.lower()]["c"]
    else:
        raise ValueError("Unknown tree type. Please use 'teak', 'pine', or add constants for your tree species.")
    
    # Convert DBH from cm to meters for consistency
    dbh_meters = dbh / 100.0
    
    # Calculate crown diameter in meters
    crown_diameter = a * (dbh_meters ** b) * (height ** c)
    
    # Calculate crown area in square meters
    crown_area = math.pi * (crown_diameter / 2) ** 2
    
    return {
        "crown_diameter": round(crown_diameter, 2),
        "crown_area": round(crown_area, 2)
    }




def simulate_tree_growth(
    initial_age, initial_height, initial_dbh, initial_volume, target_age, tree_profile,
    soil_quality, temperature_adaptation, water_availability, tree_spacing, tree_type,use_crown_in_competition=False
):
    current_age = initial_age
    current_height = initial_height
    current_dbh = initial_dbh
    current_volume = initial_volume
    
    # Initial crown size
    initial_crown_size = calculate_crown_size(current_dbh, current_height, tree_type)

    combined_growth_factor = min(soil_quality, temperature_adaptation, water_availability)
    growth_data = []

    while current_age < target_age:
        for phase in tree_profile["growth_phases"]:
            if phase["start_age"] <= current_age < phase["end_age"]:
                height_growth_rate = (phase["height_growth"] / 1000) * combined_growth_factor  # meters
                dbh_growth_rate = phase["dbh_growth"] * combined_growth_factor  # cm/year
                volume_growth_rate = phase["volume_growth"] * combined_growth_factor  # m³/year
                break

        # Calculate competition index with or without crown size
        if use_crown_in_competition:
            competition_index = calculate_uniform_competition_index(
                tree_spacing, influence_radius=10, dbh=current_dbh, crown_diameter=initial_crown_size["crown_diameter"]
            )
        else:
            competition_index = calculate_uniform_competition_index(tree_spacing, influence_radius=10, dbh=current_dbh)
        adjusted_height_growth = height_growth_rate * (1 - competition_index)
        adjusted_dbh_growth = dbh_growth_rate * (1 - competition_index)
        adjusted_volume_growth = volume_growth_rate * (1 - competition_index)

        new_height = min(adjusted_height_growth, tree_profile["max_values"]["max_height"] - current_height)
        new_dbh = min(adjusted_dbh_growth, tree_profile["max_values"]["max_canopy_diameter"] * 10 - current_dbh)
        new_volume = min(adjusted_volume_growth, tree_profile["max_values"]["max_biomass"] - current_volume)

        current_height += new_height
        current_dbh += new_dbh
        current_volume += new_volume

        collar_diameter = calculate_collar_diameter(current_dbh)

        # Calculate the crown size based on updated DBH and height
        crown = calculate_crown_size(current_dbh, current_height, tree_type)
        
        growth_data.append({
            "year": round(current_age, 2),
            "height": round(current_height, 2),
            "height_growth": round(new_height, 2),
            "dbh": round(current_dbh, 2),
            "dbh_growth": round(new_dbh, 2),
            "volume": round(current_volume, 2),
            "volume_growth": round(new_volume, 2),
            "collar_diameter": round(collar_diameter, 2),
            "crown_diameter": crown["crown_diameter"],
            "crown_area": crown["crown_area"],
            "competition_index": competition_index
        })

        current_age += 1  # Increment age by 1 year

    return {
        "final_height": round(current_height, 2),
        "final_dbh": round(current_dbh, 2),
        "final_volume": round(current_volume, 2),
        "final_collar_diameter": round(collar_diameter, 2),
        "growth_data": growth_data,
        "soil_quality": soil_quality,
        "temperature_adaptation": temperature_adaptation,
        "water_availability": water_availability,
        "final_crown_diameter": crown["crown_diameter"],
        "final_crown_area": crown["crown_area"]
    }
