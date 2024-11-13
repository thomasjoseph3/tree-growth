from SimulationBase import SimulationBase
import math

class TreeSimulation(SimulationBase):
    def __init__(self, tree, soil_quality, water_availability, temperature_adaptation, competition_index):
        super().__init__(tree)
        self.soil_quality = soil_quality
        self.water_availability = water_availability
        self.temperature_adaptation = temperature_adaptation
        self.competition_index = competition_index

    def calculate_collar_diameter(self, dbh):
        """Calculate collar diameter from DBH."""
        return 0.8692 + 1.1 * dbh

    def calculate_crown_size(self, dbh, height, tree_type):
        species_constants = {
            "teak": {"a": 1.1, "b": 0.8, "c": 0.6},
            "pine": {"a": 0.9, "b": 0.75, "c": 0.5}
        }
        if tree_type.lower() in species_constants:
            a, b, c = species_constants[tree_type.lower()].values()
        else:
            raise ValueError("Unknown tree type. Please use 'teak', 'pine', or add constants for your tree species.")

        dbh_meters = dbh / 100.0
        crown_diameter = a * (dbh_meters ** b) * (height ** c)
        crown_area = math.pi * (crown_diameter / 2) ** 2

        return {"crown_diameter": round(crown_diameter, 2), "crown_area": round(crown_area, 2)}

    def simulate_growth(self, initial_age, initial_height, initial_dbh, initial_volume, target_age, tree_spacing, use_competition=False):
        current_age = initial_age
        current_height = initial_height
        current_dbh = initial_dbh
        current_volume = initial_volume

        initial_crown_size = self.calculate_crown_size(current_dbh, current_height, self.tree.name)
        combined_growth_factor = min(self.soil_quality, self.temperature_adaptation, self.water_availability)
        print(self.soil_quality, self.temperature_adaptation, self.water_availability)
        growth_data = []

        while current_age < target_age:
            for phase in self.tree.growth_phases:
                if phase["start_age"] <= current_age < phase["end_age"]:
                    height_growth_rate = (phase["height_growth"] / 1000) * combined_growth_factor
                    dbh_growth_rate = phase["dbh_growth"] * combined_growth_factor
                    volume_growth_rate = phase["volume_growth"] * combined_growth_factor
                    break

            competition_index = self.competition_index.calculate() if use_competition else 0

            adjusted_height_growth = height_growth_rate * (1 - competition_index)
            adjusted_dbh_growth = dbh_growth_rate * (1 - competition_index)
            adjusted_volume_growth = volume_growth_rate * (1 - competition_index)

            new_height = min(adjusted_height_growth, self.tree.max_values["max_height"] - current_height)
            new_dbh = min(adjusted_dbh_growth, self.tree.max_values["max_canopy_diameter"] * 10 - current_dbh)
            new_volume = min(adjusted_volume_growth, self.tree.max_values["max_biomass"] - current_volume)

            current_height += new_height
            current_dbh += new_dbh
            current_volume += new_volume

            collar_diameter = self.calculate_collar_diameter(current_dbh)
            crown = self.calculate_crown_size(current_dbh, current_height, self.tree.name)

            growth_data.append({
                "year": round(current_age, 2),
                "height": round(current_height, 2),
                "height_growth": round(new_height, 2),
                "dbh": round(current_dbh, 2),
                "dbh_growth": round(new_dbh, 2),
                "volume": round(current_volume, 2),
                "volume_growth": round(new_volume, 2),
                "collar_diameter": round(collar_diameter, 2),
                "crown_diameter": crown["crown_diameter"],
                "crown_area": crown["crown_area"],
                "competition_index": competition_index
            })

            current_age += 1

        return {
            "final_height": round(current_height, 2),
            "final_dbh": round(current_dbh, 2),
            "final_volume": round(current_volume, 2),
            "final_collar_diameter": round(collar_diameter, 2),
            "growth_data": growth_data,
            "soil_quality": self.soil_quality,
            "temperature_adaptation": self.temperature_adaptation,
            "water_availability": self.water_availability,
            "final_crown_diameter": crown["crown_diameter"],
            "final_crown_area": crown["crown_area"]
        }
