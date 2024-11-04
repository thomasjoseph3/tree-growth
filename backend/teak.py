import math
from functions.teak.growth import calculate_growth_rate, calculate_annual_height_growth
from functions.teak.teak import TEAK_PROFILES
from functions.soil.soil_quality import calculate_soil_quality
from functions.temperature.tempreature_score_with_tolerance import calculate_temperature_adaptation
from functions.water.water_availability import calculate_water_availability


TEAK_PROFILES = {
    "teak": {
        "growth_phases": [
            { "start_age": 0, "end_age": 10, "height_growth": 2000, "dbh_growth": 7.5, "volume_growth": 0.04 },
            { "start_age": 10, "end_age": 20, "height_growth": 1200, "dbh_growth": 5.0, "volume_growth": 0.024 },
            { "start_age": 20, "end_age": 30, "height_growth": 800, "dbh_growth": 3.0, "volume_growth": 0.016 }
        ],
        "max_values": {
            "max_height": 40.0,             # meters
            "max_canopy_diameter": 15.0,    # meters, affects max DBH
            "max_biomass": 1500.0           # kg
        },
                "temperature_tolerance": {
            "cold_tolerance": 5,
            "heat_tolerance": 45
        }
    }
}


def simulate_teak_growth(
    initial_age, initial_height, initial_dbh, initial_volume, target_age, teak_profile,
    soil_quality, temperature_adaptation, water_availability
):
    current_age = initial_age
    current_height = initial_height
    current_dbh = initial_dbh
    current_volume = initial_volume

    # Calculate the combined growth factor
    combined_growth_factor = min(soil_quality, temperature_adaptation, water_availability)

    while current_age < target_age:
        # Determine the current growth phase
        for phase in teak_profile["growth_phases"]:
            if phase["start_age"] <= current_age < phase["end_age"]:
                # Apply growth factor to each growth rate
                height_growth_rate = (phase["height_growth"] / 1000) * combined_growth_factor  # meters
                dbh_growth_rate = phase["dbh_growth"] * combined_growth_factor  # cm/year
                volume_growth_rate = phase["volume_growth"] * combined_growth_factor  # m³/year
                break

        # Incrementally add growth each year, limited by max values
        new_height = min(height_growth_rate, teak_profile["max_values"]["max_height"] - current_height)
        current_height += new_height

        max_dbh = teak_profile["max_values"]["max_canopy_diameter"] * 10  # Max DBH in cm
        new_dbh = min(dbh_growth_rate, max_dbh - current_dbh)
        current_dbh += new_dbh

        new_volume = min(volume_growth_rate, teak_profile["max_values"]["max_biomass"] - current_volume)
        current_volume += new_volume

        # Print step-by-step calculations for each year
        print(f"Year {round(current_age, 2)}:")
        print(f"  Combined Growth Factor: {combined_growth_factor}")
        print(f"  Adjusted Growth Rates - Height: {height_growth_rate * 1000} mm/year, DBH: {dbh_growth_rate} mm/year, Volume: {volume_growth_rate} m³/year")
        print(f"  Updated Values - Height: {round(current_height, 4)} m, DBH: {round(current_dbh, 4)} cm, Volume: {round(current_volume, 4)} m³\n")

        # Increment age by 1 year
        current_age += 1

    return {
        "final_height": round(current_height, 2),
        "final_dbh": round(current_dbh, 2),
        "final_volume": round(current_volume, 2)
    }

soil_quality = calculate_soil_quality(
    soil_type="loamy", 
    pH=6.5, 
    tree_type="teak", 
    nitrogen=75, 
    phosphorus=35, 
    potassium=40, 
    organic_matter=28
)           
temperature_adaptation =calculate_temperature_adaptation(33, (20, 30), 5, 45)
water_availability = calculate_water_availability(1200,"loamy","moderately_drained")         # Between 0 and 1


# Define initial conditions
initial_age = 10       # 4 months, converted to years
initial_height = 20.5    # meters
initial_dbh = 77.0        # cm
initial_volume = 0.41    # cubic meters
target_age = 20     # years

# Run simulation
growth_result = simulate_teak_growth(
    initial_age=initial_age, 
    initial_height=initial_height, 
    initial_dbh=initial_dbh, 
    initial_volume=initial_volume, 
    target_age=target_age, 
    teak_profile=TEAK_PROFILES["teak"],
    temperature_adaptation=temperature_adaptation,
    soil_quality=soil_quality,
    water_availability=water_availability
)

print("Growth after", target_age, "years:", growth_result)
