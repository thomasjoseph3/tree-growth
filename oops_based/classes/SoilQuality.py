# Soil.py

import math

class SoilQuality:
    SOIL_BASE_QUALITY = {
        "loamy": 0.9,
        "sandy": 0.5,
        "clay": 0.5,
        "silt": 0.6,
        "laterite": 0.6,
        "peaty": 0.8,
        "black cotton": 0.55,
        "alluvial": 0.85
    }

    def __init__(self, soil_type, pH, nitrogen, phosphorus, potassium, organic_matter):
        self.soil_type = soil_type.lower()
        self.pH = pH
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.organic_matter = organic_matter

    def calculate_nutrient_factor(self, tree):
        ideal_levels = tree.ideal_nutrient_levels
        weights = tree.nutrient_weights

        # Calculate nutrient factors, capped at 1 if actual > ideal
        nitrogen_factor = min(self.nitrogen / ideal_levels["nitrogen"], 1.0)
        phosphorus_factor = min(self.phosphorus / ideal_levels["phosphorus"], 1.0)
        potassium_factor = min(self.potassium / ideal_levels["potassium"], 1.0)
        organic_matter_factor = min(self.organic_matter / ideal_levels["organic_matter"], 1.0)

        # Calculate weighted nutrient factor
        nutrient_factor = (
            (nitrogen_factor * weights["nitrogen"]) +
            (phosphorus_factor * weights["phosphorus"]) +
            (potassium_factor * weights["potassium"]) +
            (organic_matter_factor * weights["organic_matter"])
        )

        return round(nutrient_factor, 2)

    def calculate_soil_quality(self, tree):
        base_quality = self.SOIL_BASE_QUALITY.get(self.soil_type, 0.5)
        tree_prefs = tree.soil_preferences
        nutrient_factor = self.calculate_nutrient_factor(tree)

        if self.soil_type in tree_prefs["preferred_soils"]:
            min_pH, max_pH = tree_prefs["pH_range"]
            tolerance = tree_prefs["pH_tolerance"]

            # Calculate pH deviation if outside ideal range
            pH_deviation = max(0, abs(self.pH - min(min_pH, max_pH)) - tolerance)
            penalty = min(0.5, math.log(1 + (pH_deviation / tolerance))) if pH_deviation else 0
            final_quality = max((base_quality - penalty) * nutrient_factor, 0)
        else:
            final_quality = max((base_quality * 0.5) * nutrient_factor, 0)

        return round(final_quality, 2)
