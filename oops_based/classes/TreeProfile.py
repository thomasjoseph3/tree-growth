class TreeProfile:
    def __init__(self, name, growth_phases, max_values, temperature_tolerance, water_range, soil_preferences):
        self.name = name
        self.growth_phases = growth_phases
        self.max_values = max_values
        self.temperature_tolerance = temperature_tolerance
        self.water_range = water_range
        self.soil_preferences = soil_preferences

    def display(self):
        """Display details of the tree profile."""
        print(f"Tree Profile: {self.name}")
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
        print(f"  Cold Tolerance: {self.temperature_tolerance['cold_tolerance']}°C, "
              f"Heat Tolerance: {self.temperature_tolerance['heat_tolerance']}°C")
        print(f"Water Range: {self.water_range[0]} - {self.water_range[1]} mm")
        print("Soil Preferences:")
        print(f"  Preferred Soils: {', '.join(self.soil_preferences['preferred_soils'])}")
        print(f"  pH Range: {self.soil_preferences['pH_range'][0]} - {self.soil_preferences['pH_range'][1]}")
        print(f"  pH Tolerance: ±{self.soil_preferences['pH_tolerance']}")
        print("\n")





