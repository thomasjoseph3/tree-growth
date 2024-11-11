from functions.trees_spec import TREE_PROFILES
from tree_calc.simulation_with_ci import simulate_tree_growth
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
    tree_spacing,
    conditions
):
    results_per_condition = []

    # Variables to accumulate weighted averages
    total_height, total_dbh, total_volume, total_collar_diameter = 0, 0, 0, 0
    total_trees_count = 0

    for condition in conditions:
        proportion = float(condition['proportion'])
        area_acres_for_condition = total_area_acres * proportion
        trees_in_condition = int(total_trees * proportion)

        # Calculate environmental factors
        soil_quality = calculate_soil_quality(
            soil_type=condition['soil_type'],
            pH=float(condition['pH']),
            tree_type=tree_type,
            nitrogen=float(condition['nitrogen']),
            phosphorus=float(condition['phosphorus']),
            potassium=float(condition['potassium']),
            organic_matter=float(condition['organic_matter'])
        )
        temperature_adaptation = calculate_temperature_adaptation(
            average_temp=float(condition['temp']),
            optimal_temp_range=(float(condition['min_temp']), float(condition['max_temp'])),
            cold_tolerance=float(condition['cold_tolerance']),
            heat_tolerance=float(condition['heat_tolerance'])
        )
        water_availability = calculate_water_availability(
            annual_rainfall=float(condition['annual_rainfall']),
            soil_type=condition['soil_type'],
            drainage=condition['drainage'],
            tree_type=tree_type
        )

        # Run simulation
        growth_result = simulate_tree_growth(
            initial_age=initial_age,
            initial_height=initial_height,
            initial_dbh=initial_dbh,
            initial_volume=initial_volume,
            target_age=target_age,
            tree_profile=TREE_PROFILES[tree_type],
            soil_quality=soil_quality,
            temperature_adaptation=temperature_adaptation,
            water_availability=water_availability,
            tree_spacing=tree_spacing
        )

        # Weighted accumulation for each metric
        total_height += growth_result["final_height"] * trees_in_condition
        total_dbh += growth_result["final_dbh"] * trees_in_condition
        total_volume += growth_result["final_volume"] * trees_in_condition
        total_collar_diameter += growth_result["final_collar_diameter"] * trees_in_condition
        total_trees_count += trees_in_condition

        results_per_condition.append({
            "condition_proportion": proportion,
            "trees_in_condition": trees_in_condition,
            "area_acres_for_condition": area_acres_for_condition,
            "average_growth": {
                "average_final_height": growth_result["final_height"],
                "average_final_dbh": growth_result["final_dbh"],
                "average_final_volume": growth_result["final_volume"],
                "average_collar_diameter": growth_result["final_collar_diameter"]
            }
        })

    # Calculate overall weighted averages
    average_height = total_height / total_trees_count
    average_dbh = total_dbh / total_trees_count
    average_volume = total_volume / total_trees_count
    average_collar_diameter = total_collar_diameter / total_trees_count

    return {
        "total_trees": total_trees,
        "total_area_acres": total_area_acres,
        "overall_average_growth": {
            "average_height": round(average_height, 2),
            "average_dbh": round(average_dbh, 2),
            "average_volume": round(average_volume, 2),
            "average_collar_diameter": round(average_collar_diameter, 2)
        },
        "results_per_condition": results_per_condition
    }
