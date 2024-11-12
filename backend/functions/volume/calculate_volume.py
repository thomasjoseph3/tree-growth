def calculate_tree_volume(dbh, height, tree_type):
    # Define empirical coefficients for each species
    species_coefficients = {
        "teak": {"b1": 0.000056, "b2": 2.524, "b3": 0.705},
        "pine": {"b1": 0.000046, "b2": 2.499, "b3": 0.701},
        "eucalyptus": {"b1": 0.000065, "b2": 2.6, "b3": 0.73}
    }
    
    # Retrieve the coefficients based on tree type
    if tree_type.lower() in species_coefficients:
        b1 = species_coefficients[tree_type.lower()]["b1"]
        b2 = species_coefficients[tree_type.lower()]["b2"]
        b3 = species_coefficients[tree_type.lower()]["b3"]
    else:
        raise ValueError("Unknown tree type. Use 'teak', 'pine', or 'eucalyptus'.")

    # Calculate volume using the specific allometric equation
    volume = b1 * (dbh ** b2) * (height ** b3)
    return volume
