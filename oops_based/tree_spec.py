TREE_PROFILES = {
    "teak": {
        "growth_phases": [
            { "start_age": 0, "end_age": 10, "height_growth": 1000, "dbh_growth": 1.8, "volume_growth": 0.03 },
            { "start_age": 10, "end_age": 20, "height_growth": 700, "dbh_growth": 1.3, "volume_growth": 0.035 },
            { "start_age": 20, "end_age": 30, "height_growth": 300, "dbh_growth": 0.8, "volume_growth": 0.015 }
        ],
        "max_values": {
            "max_height": 35.0, "max_canopy_diameter": 9.0, "max_biomass": 1300.0
        },
        "temperature_tolerance": {
            "cold_tolerance": 5, "heat_tolerance": 45
        },
        "water_range": (1200, 2500),
        "soil_preferences": {
            "preferred_soils": ["loamy", "sandy"],
            "pH_range": (6, 7.5),
            "pH_tolerance": 3
        },
        "ideal_nutrient_levels": {"nitrogen": 80, "phosphorus": 40, "potassium": 40, "organic_matter": 30},
        "nutrient_weights": {"nitrogen": 0.4, "phosphorus": 0.2, "potassium": 0.2, "organic_matter": 0.2}
    },
    "pine": {
        "growth_phases": [
            { "start_age": 0, "end_age": 10, "height_growth": 800, "dbh_growth": 1.5, "volume_growth": 0.025 },
            { "start_age": 10, "end_age": 20, "height_growth": 500, "dbh_growth": 1.2, "volume_growth": 0.03 },
            { "start_age": 20, "end_age": 40, "height_growth": 200, "dbh_growth": 0.7, "volume_growth": 0.02 }
        ],
        "max_values": {
            "max_height": 30.0, "max_canopy_diameter": 8.0, "max_biomass": 1000.0
        },
        "temperature_tolerance": {
            "cold_tolerance": -10, "heat_tolerance": 40
        },
        "water_range": (700, 1500),
        "soil_preferences": {
            "preferred_soils": ["sandy", "loamy", "alluvial"],
            "pH_range": (4.5, 6.5),
            "pH_tolerance": 2.5
        },
        "ideal_nutrient_levels": {"nitrogen": 65, "phosphorus": 30, "potassium": 35, "organic_matter": 20},
        "nutrient_weights": {"nitrogen": 0.3, "phosphorus": 0.25, "potassium": 0.25, "organic_matter": 0.2}
    },
    "eucalyptus": {
        "growth_phases": [
            { "start_age": 0, "end_age": 10, "height_growth": 1200, "dbh_growth": 2.0, "volume_growth": 0.04 },
            { "start_age": 10, "end_age": 20, "height_growth": 800, "dbh_growth": 1.5, "volume_growth": 0.05 },
            { "start_age": 20, "end_age": 30, "height_growth": 300, "dbh_growth": 1.0, "volume_growth": 0.03 }
        ],
        "max_values": {
            "max_height": 40.0, "max_canopy_diameter": 10.0, "max_biomass": 1500.0
        },
        "temperature_tolerance": {
            "cold_tolerance": 0, "heat_tolerance": 50
        },
        "water_range": (800, 1800),
        "soil_preferences": {
            "preferred_soils": ["loamy", "clay", "laterite"],
            "pH_range": (5, 7),
            "pH_tolerance": 2
        },
        "ideal_nutrient_levels": {"nitrogen": 75, "phosphorus": 35, "potassium": 40, "organic_matter": 25},
        "nutrient_weights": {"nitrogen": 0.35, "phosphorus": 0.25, "potassium": 0.2, "organic_matter": 0.2}
    }
}
