import math
from functions.trees_spec import TREE_PROFILES
from tree_calc.simulate_tree import simulate_tree_growth
from functions.soil.soil_quality import calculate_soil_quality
from functions.temperature.tempreature_score_with_tolerance import calculate_temperature_adaptation
from functions.water.water_availability import calculate_water_availability

def area_growth_calculation(
    area_acres, tree_density_per_acre, initial_age, initial_height, initial_dbh, 
    initial_volume, target_age, tree_type, soil_type, pH, nitrogen, phosphorus, 
    potassium, organic_matter, temp, min_temp, max_temp, cold_tolerance, 
    heat_tolerance, annual_rainfall, drainage
):
    """
    Calculates the total expected growth of trees across an area by scaling up from a single tree simulation.
    """
    
    # Calculate total number of trees based on area and density
    total_trees = math.ceil(area_acres * tree_density_per_acre)

    # Calculate soil quality
    soil_quality = calculate_soil_quality(
        soil_type=soil_type,
        pH=pH,
        tree_type=tree_type,
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=potassium,
        organic_matter=organic_matter
    )

    # Calculate temperature adaptation
    temperature_adaptation = calculate_temperature_adaptation(
        temp,
        (min_temp, max_temp),
        cold_tolerance,
        heat_tolerance
    )

    # Calculate water availability
    water_availability = calculate_water_availability(
        annual_rainfall,
        soil_type,
        drainage
    )

    # Run the growth simulation for a single tree
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

    # Scale up the growth results for the entire area
    aggregated_result = {
        "total_final_height": growth_result["final_height"] * total_trees,
        "total_final_dbh": growth_result["final_dbh"] * total_trees,
        "total_final_volume": growth_result["final_volume"] * total_trees,
        "total_collar_diameter": growth_result["final_collar_diameter"] * total_trees,
    }

    return {
        "total_trees": total_trees,
        "aggregated_growth": aggregated_result
    }
