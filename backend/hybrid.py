import math
def logistic_growth(t, Hmax, k, t0):
    """
    Calculate baseline tree height at time t using the Logistic Growth Model.

    Parameters:
    - t (float): Time in years
    - Hmax (float): Maximum attainable height
    - k (float): Growth rate parameter
    - t0 (float): Time of inflection point

    Returns:
    - float: Baseline height at time t
    """
    return Hmax / (1 + math.exp(-k * (t - t0)))

def calculate_tree_growth(
    t, Hmax, k, t0, 
    soil_quality, 
    water_availability, 
    temperature_adaptation
):
    """
    Calculate adjusted tree height at time t using a hybrid growth model.

    Parameters:
    - t (float): Time in years
    - Hmax (float): Maximum attainable height
    - k (float): Growth rate parameter
    - t0 (float): Time of inflection point
    - soil_quality (float): Soil quality score (0-1)
    - water_availability (float): Water availability score (0-1)
    - temperature_adaptation (float): Temperature adaptation score (0-1)

    Returns:
    - float: Adjusted tree height at time t
    """

    # Baseline height from Logistic Growth Model
    baseline_height = logistic_growth(t, Hmax, k, t0)

    # Combined environmental adjustment factor
    # Average of all three factors, or you could apply weights if desired
    adjustment_factor = (soil_quality + water_availability + temperature_adaptation) / 3

    # Adjust baseline growth by environmental factors
    adjusted_height = baseline_height * adjustment_factor

    return round(adjusted_height, 2)

# Example usage
t = 5  # For 5 years of growth
Hmax = 30  # Example max height in meters
k = 0.2  # Example growth rate for teak
t0 = 3  # Example inflection point

# Environmental scores (from your previously defined functions)
soil_quality = 0.72  # Example score
water_availability = 0.85  # Example score
temperature_adaptation = 0.9  # Example score

tree_height = calculate_tree_growth(
    t, Hmax, k, t0, 
    soil_quality, 
    water_availability, 
    temperature_adaptation
)

print("Adjusted Tree Height after", t, "years:", tree_height)
