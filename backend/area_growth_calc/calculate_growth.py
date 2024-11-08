import math
from functions.trees_spec import TREE_PROFILES
from tree_calc.simulate_tree import simulate_tree_growth
from functions.soil.soil_quality import calculate_soil_quality
from functions.temperature.tempreature_score_with_tolerance import calculate_temperature_adaptation
from functions.water.water_availability import calculate_water_availability

def area_growth_calculation(
    total_area_acres, 
    total_trees, 
    initial_age, 
    initial_height, 
    initial_dbh, 
    initial_volume, 
    target_age, 
    tree_type, 
    conditions
):
    """
    Calculates the expected growth of trees across an area with varied conditions.
    
    Parameters:
    - total_area_acres (float): Total area in acres.
    - total_trees (int): Total number of trees across the plantation.
    - initial_age, initial_height, initial_dbh, initial_volume (float): Initial metrics of the trees.
    - target_age (int): Target age to calculate growth to.
    - tree_type (str): Type of tree.
    - conditions (list): List of dictionaries with conditions for each section of the area.
    
    Returns:
    - dict: Average growth metrics and tree counts per condition.
    """
    
    # List to store growth results for each condition
    results_per_condition = []

    # Calculate growth for each condition
    for condition in conditions:
        # Calculate the area and number of trees for this specific condition
        proportion = float(condition['proportion'])
        area_acres_for_condition = total_area_acres * proportion
        trees_in_condition = int(total_trees * proportion)

        # Calculate soil quality
        soil_quality = calculate_soil_quality(
            soil_type=condition['soil_type'],
            pH=float(condition['pH']),
            tree_type=tree_type,
            nitrogen=float(condition['nitrogen']),
            phosphorus=float(condition['phosphorus']),
            potassium=float(condition['potassium']),
            organic_matter=float(condition['organic_matter'])
        )

        # Calculate temperature adaptation
        temperature_adaptation = calculate_temperature_adaptation(
            average_temp=float(condition['temp']),
            optimal_temp_range=(float(condition['min_temp']), float(condition['max_temp'])),
            cold_tolerance=float(condition['cold_tolerance']),
            heat_tolerance=float(condition['heat_tolerance'])
        )

        # Calculate water availability
        water_availability = calculate_water_availability(
            annual_rainfall=float(condition['annual_rainfall']),
            soil_type=condition['soil_type'],
            drainage=condition['drainage'],
            tree_type=tree_type
        )

        # Run growth simulation for a single tree in this condition
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

        # Calculate average growth per tree in this condition
        average_growth = {
            "average_final_height": growth_result["final_height"],
            "average_final_dbh": growth_result["final_dbh"],
            "average_final_volume": growth_result["final_volume"],
            "average_collar_diameter": growth_result["final_collar_diameter"]
        }

        # Append the results for this condition
        results_per_condition.append({
            "condition_proportion": proportion,
            "trees_in_condition": trees_in_condition,
            "area_acres_for_condition": area_acres_for_condition,
            "average_growth": average_growth
        })

    # Return growth details for each condition in the plantation area
    return {
        "total_trees": total_trees,
        "total_area_acres": total_area_acres,
        "results_per_condition": results_per_condition
    }
