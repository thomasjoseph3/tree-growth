from classes.TreeProfile import TreeProfile

class TreeProfileManager:
    def __init__(self):
        self.tree_profiles = {}

    def add_tree_profile(self, name, growth_phases, max_values, temperature_tolerance, water_range, soil_preferences):
        """Add a new tree profile to the collection."""
        self.tree_profiles[name] = TreeProfile(name, growth_phases, max_values, temperature_tolerance, water_range, soil_preferences)

    def display_all_profiles(self):
        """Display all tree profiles."""
        for profile in self.tree_profiles.values():
            profile.display()