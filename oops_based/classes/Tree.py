import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tree_spec import TREE_PROFILES
class Tree:
    def __init__(self, name, profile):
        self.name = name
        self.growth_phases = profile.get("growth_phases", [])
        self.max_values = profile.get("max_values", {})
        self.temperature_tolerance = profile.get("temperature_tolerance", {})
        self.water_range = profile.get("water_range", (0, 0))
        self.soil_preferences = profile.get("soil_preferences", {})
        self.ideal_nutrient_levels = profile.get("ideal_nutrient_levels",{})
        self.nutrient_weights = profile.get("nutrient_weights",{})
    

    def display(self):
        """Display details of the tree profile."""
        print(f"Tree Profile: {self.name.capitalize()}")
        print("Growth Phases:")
        for phase in self.growth_phases:
            print(f"  Age {phase['start_age']}-{phase['end_age']}: "
                  f"Height Growth: {phase['height_growth']} mm/year, "
                  f"DBH Growth: {phase['dbh_growth']} cm/year, "
                  f"Volume Growth: {phase['volume_growth']} m³/year")
        print("Max Values:")
        for key, value in self.max_values.items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value}")
        print("Temperature Tolerance:")
        print(f"  Cold Tolerance: {self.temperature_tolerance.get('cold_tolerance')}°C, "
              f"Heat Tolerance: {self.temperature_tolerance.get('heat_tolerance')}°C")
        print(f"Water Range: {self.water_range[0]} - {self.water_range[1]} mm")
        print("Soil Preferences:")
        print(f"  Preferred Soils: {', '.join(self.soil_preferences.get('preferred_soils', []))}")
        print(f"  pH Range: {self.soil_preferences.get('pH_range', (0, 0))[0]} - {self.soil_preferences.get('pH_range', (0, 0))[1]}")
        print(f"  pH Tolerance: ±{self.soil_preferences.get('pH_tolerance', 0)}")
        print("\n")

# # Example usage

# # Creating tree objects from TREE_PROFILES data
# teak_tree = Tree("teak", TREE_PROFILES["teak"])
# pine_tree = Tree("pine", TREE_PROFILES["pine"])
# eucalyptus_tree = Tree("eucalyptus", TREE_PROFILES["eucalyptus"])
