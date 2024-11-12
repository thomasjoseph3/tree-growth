def empirical_growth_prediction(initial_age, initial_height, initial_dbh, initial_volume, target_age, site_factor):
    # Teak tree specific constants
    a, b, c = 0.5, 0.7, -0.2  # DBH increment model coefficients
    d, e, f = 0.1, 0.8, -0.2  # Adjusted height growth model coefficients
    g, h, i = 0.0001, 2.5, 1.3  # Volume model coefficients

    current_age = initial_age
    current_height = initial_height
    current_dbh = initial_dbh  # Initialize DBH with initial value
    current_volume = initial_volume

    growth_data = []

    while current_age < target_age:
        # Calculate DBH increment
        dbh_increment = a * (current_dbh ** b) * (current_age ** c) * site_factor
        current_dbh += dbh_increment

        # Calculate height increment
        height_increment = d * (current_height ** e) * (current_age ** f) * site_factor
        current_height += height_increment

        # Calculate volume
        current_volume = g * (current_dbh ** h) * (current_height ** i)

        # Store growth data for this year
        growth_data.append({
            "age": round(current_age, 2),
            "dbh": round(current_dbh, 2),
            "dbh_increment": round(dbh_increment, 2),
            "height": round(current_height, 2),
            "height_increment": round(height_increment, 2),
            "volume": round(current_volume, 5)
        })

        # Increment age by 1 year
        current_age += 1

    return {
        "final_age": round(current_age - 1, 2),
        "final_dbh": round(current_dbh, 2),
        "final_height": round(current_height, 2),
        "final_volume": round(current_volume, 5),
        "growth_data": growth_data
    }

# Testing the function with sample data
data = empirical_growth_prediction(0.3, 10, 2, 0.5, 10, 1)
print(data)
