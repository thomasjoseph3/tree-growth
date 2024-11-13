import math

class CompetitionIndex:
    def __init__(self, tree_spacing, influence_radius, dbh, crown_diameter=None, max_density=50):
        self.tree_spacing = tree_spacing
        self.influence_radius = influence_radius
        self.dbh = dbh
        self.crown_diameter = crown_diameter
        self.max_density = max_density

    def calculate(self):
        if self.crown_diameter:
            adjusted_influence_radius = self.influence_radius + (self.crown_diameter / 2)
        else:
            adjusted_influence_radius = self.influence_radius

        influence_area = math.pi * (adjusted_influence_radius ** 2)
        tree_density = 1 / (self.tree_spacing ** 2)
        expected_trees_in_area = influence_area * tree_density
        growth_competition_factor = math.sqrt(self.dbh / 10)
        density_factor = min((expected_trees_in_area * growth_competition_factor) / self.max_density, 1.0)

        return round(density_factor, 2)
