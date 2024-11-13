import math

class CompetitionIndex:
    def __init__(self, tree_spacing, influence_radius, dbh, crown_diameter=None, max_density=50):
        """
        Initialize competition index parameters.

        Parameters:
        - tree_spacing (float): Initial distance between trees in meters.
        - influence_radius (float): Base radius defining the area of influence around each tree.
        - dbh (float): Diameter at breast height (DBH) of the tree in cm.
        - crown_diameter (float, optional): Diameter of the tree's crown in meters.
        - max_density (int): Maximum density in the influence area for scaling.
        """
        self.tree_spacing = tree_spacing
        self.influence_radius = influence_radius
        self.dbh = dbh
        self.crown_diameter = crown_diameter
        self.max_density = max_density

    def calculate(self):
        """
        Calculate and return the competition index.

        Returns:
        - float: Competition index, where higher values indicate more competition.
        """
        # Adjust influence radius to include half of the crown diameter if specified
        if self.crown_diameter:
            adjusted_influence_radius = self.influence_radius + (self.crown_diameter / 2)
        else:
            adjusted_influence_radius = self.influence_radius

        # Calculate the area of influence in square meters
        influence_area = math.pi * (adjusted_influence_radius ** 2)

        # Calculate density of trees per square meter based on spacing
        tree_density = 1 / (self.tree_spacing ** 2)

        # Calculate number of trees expected within the influence area
        expected_trees_in_area = influence_area * tree_density

        # Introduce a multiplier based on DBH to simulate increased competition as the tree grows
        growth_competition_factor = math.sqrt(self.dbh / 10)

        # Normalize by max_density to keep value between 0 and 1
        density_factor = min((expected_trees_in_area * growth_competition_factor) / self.max_density, 1.0)

        # Return the competition index
        return round(density_factor, 2)
