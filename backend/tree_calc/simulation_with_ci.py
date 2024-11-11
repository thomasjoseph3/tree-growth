from functions.competition.competition_index import calculate_uniform_competition_index
def calculate_collar_diameter(dbh):
    return 0.8692 + 1.1 * dbh  # DBH in cm, output also in cm

def simulate_tree_growth(
    initial_age, initial_height, initial_dbh, initial_volume, target_age, tree_profile,
    soil_quality, temperature_adaptation, water_availability,tree_spacing
):  
    current_age = initial_age
    current_height = initial_height
    current_dbh = initial_dbh
    current_volume = initial_volume

    combined_growth_factor = min(soil_quality, temperature_adaptation, water_availability)
    
    # Store data for each year to send to the frontend
    growth_data = []
    previous_height, previous_dbh, previous_volume = current_height, current_dbh, current_volume

    while current_age < target_age:
        for phase in tree_profile["growth_phases"]:
            if phase["start_age"] <= current_age < phase["end_age"]:
                height_growth_rate = (phase["height_growth"] / 1000) * combined_growth_factor  # meters
                dbh_growth_rate = phase["dbh_growth"] * combined_growth_factor  # cm/year
                volume_growth_rate = phase["volume_growth"] * combined_growth_factor  # m³/year
                break
                    # Update competition index based on current DBH and spacing
        competition_index = calculate_uniform_competition_index(
            tree_spacing, influence_radius=10, dbh=current_dbh
        )
        # Adjust growth factors by competition (competition reduces growth over time)
        adjusted_height_growth = height_growth_rate * (1 - competition_index)
        adjusted_dbh_growth = dbh_growth_rate * (1 - competition_index)
        adjusted_volume_growth = volume_growth_rate * (1 - competition_index)

        # Calculate new growth for this year
        new_height = min(adjusted_height_growth, tree_profile["max_values"]["max_height"] - current_height)
        new_dbh = min(adjusted_dbh_growth, tree_profile["max_values"]["max_canopy_diameter"] * 10 - current_dbh)
        new_volume = min(adjusted_volume_growth, tree_profile["max_values"]["max_biomass"] - current_volume)

        # Update totals
        current_height += new_height
        current_dbh += new_dbh
        current_volume += new_volume

        collar_diameter = calculate_collar_diameter(current_dbh)

        growth_data.append({
            "year": round(current_age, 2),
            "height": round(current_height, 2),
            "height_growth": round(new_height, 2),
            "dbh": round(current_dbh, 2),
            "dbh_growth": round(new_dbh, 2),
            "volume": round(current_volume, 2),
            "volume_growth": round(new_volume, 2),
            "collar_diameter": round(collar_diameter, 2),
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
        "water_availability": water_availability
    }
