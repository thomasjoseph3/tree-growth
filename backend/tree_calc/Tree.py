class TreeProfile:
    def __init__(self, 
                 tree_type,
                 ideal_nutrient_levels,
                 nutrient_weights,
                 water_range,
                 growth_phases,
                 max_values,
                 temperature_tolerance,
                 preferred_soils,
                 pH_range,
                 pH_tolerance):
        """
        Initialize the TreeProfile with various attributes.
        
        Parameters:
        - tree_type (str): Type of tree (e.g., "teak", "pine").
        - ideal_nutrient_levels (dict): Dict of ideal nutrient levels.
        - nutrient_weights (dict): Dict of nutrient weights.
        - water_range (tuple): Tuple for water range (min, max).
        - growth_phases (list): List of dicts representing growth phases.
        - max_values (dict): Dict with max height, canopy diameter, and biomass.
        - temperature_tolerance (dict): Dict with cold and heat tolerance.
        - preferred_soils (list): List of preferred soil types (e.g., ["loamy", "sandy"]).
        - pH_range (tuple): Tuple indicating the ideal pH range (min, max).
        - pH_tolerance (float): Maximum pH deviation the tree can tolerate.
        """
        self.tree_type = tree_type
        self.ideal_nutrient_levels = ideal_nutrient_levels
        self.nutrient_weights = nutrient_weights
        self.water_range = water_range
        self.growth_phases = growth_phases
        self.max_values = max_values
        self.temperature_tolerance = temperature_tolerance
        self.preferred_soils = preferred_soils
        self.pH_range = pH_range
        self.pH_tolerance = pH_tolerance

    def get_growth_phases(self):
        return self.growth_phases

    def get_max_values(self):
        return self.max_values

    def get_temperature_tolerance(self):
        return self.temperature_tolerance

    def get_ideal_nutrient_levels(self):
        return self.ideal_nutrient_levels

    def get_nutrient_weights(self):
        return self.nutrient_weights

    def get_water_range(self):
        return self.water_range

    def get_soil_preferences(self):
        return {
            "preferred_soils": self.preferred_soils,
            "pH_range": self.pH_range,
            "pH_tolerance": self.pH_tolerance
        }


teak_profile = TreeProfile(
    tree_type="teak",
    ideal_nutrient_levels={"nitrogen": 80, "phosphorus": 40, "potassium": 40, "organic_matter": 30},
    nutrient_weights={"nitrogen": 0.4, "phosphorus": 0.2, "potassium": 0.2, "organic_matter": 0.2},
    water_range=(1200, 2500),
    growth_phases=[
        {"start_age": 0, "end_age": 10, "height_growth": 1000, "dbh_growth": 1.8, "volume_growth": 0.03},
        {"start_age": 10, "end_age": 20, "height_growth": 700, "dbh_growth": 1.3, "volume_growth": 0.035},
        {"start_age": 20, "end_age": 30, "height_growth": 300, "dbh_growth": 0.8, "volume_growth": 0.015}
    ],
    max_values={"max_height": 35.0, "max_canopy_diameter": 9.0, "max_biomass": 1300.0},
    temperature_tolerance={"cold_tolerance": 5, "heat_tolerance": 45},
    preferred_soils=["loamy", "sandy"],
    pH_range=(6, 7.5),
    pH_tolerance=3
)

pine_profile = TreeProfile(
    tree_type="pine",
    ideal_nutrient_levels={"nitrogen": 65, "phosphorus": 30, "potassium": 35, "organic_matter": 20},
    nutrient_weights={"nitrogen": 0.3, "phosphorus": 0.25, "potassium": 0.25, "organic_matter": 0.2},
    water_range=(700, 1500),
    growth_phases=[
        {"start_age": 0, "end_age": 10, "height_growth": 800, "dbh_growth": 1.5, "volume_growth": 0.025},
        {"start_age": 10, "end_age": 20, "height_growth": 500, "dbh_growth": 1.2, "volume_growth": 0.03},
        {"start_age": 20, "end_age": 40, "height_growth": 200, "dbh_growth": 0.7, "volume_growth": 0.02}
    ],
    max_values={"max_height": 30.0, "max_canopy_diameter": 8.0, "max_biomass": 1000.0},
    temperature_tolerance={"cold_tolerance": -10, "heat_tolerance": 40},
    preferred_soils=["sandy", "loamy", "alluvial"],
    pH_range=(4.5, 6.5),
    pH_tolerance=2.5
)

# Eucalyptus profile
eucalyptus_profile = TreeProfile(
    tree_type="eucalyptus",
    ideal_nutrient_levels={"nitrogen": 75, "phosphorus": 35, "potassium": 40, "organic_matter": 25},
    nutrient_weights={"nitrogen": 0.35, "phosphorus": 0.25, "potassium": 0.2, "organic_matter": 0.2},
    water_range=(800, 1800),
    growth_phases=[
        {"start_age": 0, "end_age": 10, "height_growth": 1200, "dbh_growth": 2.0, "volume_growth": 0.04},
        {"start_age": 10, "end_age": 20, "height_growth": 800, "dbh_growth": 1.5, "volume_growth": 0.05},
        {"start_age": 20, "end_age": 30, "height_growth": 300, "dbh_growth": 1.0, "volume_growth": 0.03}
    ],
    max_values={"max_height": 40.0, "max_canopy_diameter": 10.0, "max_biomass": 1500.0},
    temperature_tolerance={"cold_tolerance": 0, "heat_tolerance": 50},
    preferred_soils=["loamy", "clay", "laterite"],
    pH_range=(5, 7),
    pH_tolerance=2
)
