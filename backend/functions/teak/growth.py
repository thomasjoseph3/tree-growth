
def calculate_growth_rate(soil_quality, temperature_adaptation, water_availability):
    # Adjust weights as necessary to reflect the importance of each factor
    growth_rate = (soil_quality * 0.4) + (temperature_adaptation * 0.3) + (water_availability * 0.3)
    return round(growth_rate, 2)

def estimate_canopy_increase(growth_rate, current_canopy_diameter):
    # Use logistic growth or similar model
    canopy_increase = growth_rate * 0.1 * current_canopy_diameter  # Scale as needed
    return round(canopy_increase, 2)

def estimate_biomass_increase(growth_rate, current_biomass, species_factor=1.2):
    # Biomass increase based on growth rate and species factor
    biomass_increase = current_biomass * growth_rate * species_factor
    return round(biomass_increase, 2)

def calculate_annual_height_growth(growth_rate, current_height, height_factor=0.05):
    height_increase = current_height * growth_rate * height_factor
    return round(height_increase, 2)

def estimate_root_growth(biomass_increase, root_to_shoot_ratio=0.3):
    root_growth = biomass_increase * root_to_shoot_ratio
    return round(root_growth, 2)
