import math

def calculate_uniform_competition_index(tree_spacing, influence_radius, dbh, crown_diameter=None, max_density=50):
    """
    Calculate competition index for a uniformly spaced plantation based on spacing, influence area, DBH growth, and optional crown size.

    Parameters:
    - tree_spacing (float): Initial distance between trees in meters.
    - influence_radius (float): Base radius defining the area of influence around each tree.
    - dbh (float): Diameter at breast height (DBH) of the tree in cm, representing its current size.
    - crown_diameter (float, optional): Diameter of the tree's crown in meters, to increase competition if used.
    - max_density (int): Maximum density in the influence area for scaling (depends on plantation layout).

    Returns:
    - float: Competition index, where higher values indicate more competition.
    """
    # Adjust influence radius to include half of the crown diameter if specified
    if crown_diameter:
        influence_radius += crown_diameter / 2

    # Calculate the area of influence in square meters
    influence_area = math.pi * (influence_radius ** 2)

    # Calculate density of trees per square meter based on spacing
    tree_density = 1 / (tree_spacing ** 2)  # trees per square meter

    # Calculate number of trees expected within the influence area
    expected_trees_in_area = influence_area * tree_density

    # Introduce a multiplier based on DBH to simulate increased competition as tree grows
    growth_competition_factor = math.sqrt(dbh / 10)
    
    # Normalize by max_density to keep value between 0 and 1
    density_factor = min((expected_trees_in_area * growth_competition_factor) / max_density, 1.0)
    print(density_factor)
    # Return the competition index
    return round(density_factor, 2)

# # Example usage without crown size
# fac = calculate_uniform_competition_index(6.36, 5, 20)
# print("Competition Index without Crown:", fac)

# # Example usage with crown size
# fac_with_crown = calculate_uniform_competition_index(6.36, 5, 20, crown_diameter=2.5)
# print("Competition Index with Crown:", fac_with_crown)

# def calculate_uniform_competition_index(tree_spacing, influence_radius, dbh, max_density=50):
#     """
#     Calculate competition index for a uniformly spaced plantation based on spacing, influence area, and DBH growth.

#     Parameters:
#     - tree_spacing (float): Initial distance between trees in meters.
#     - influence_radius (float): Radius defining the area of influence around each tree.
#     - dbh (float): Diameter at breast height (DBH) of the tree in cm, representing its current size.
#     - max_density (int): Maximum density in the influence area for scaling (depends on plantation layout).

#     Returns:
#     - float: Competition index, where higher values indicate more competition.
#     """
#     # Calculate the area of influence in square meters
#     influence_area = math.pi * (influence_radius ** 2)

#     # Calculate density of trees per square meter based on spacing
#     tree_density = 1 / (tree_spacing ** 2)  # trees per square meter

#     # Calculate number of trees expected within the influence area
#     expected_trees_in_area = influence_area * tree_density

#     # Introduce a multiplier based on DBH to simulate increased competition as tree grows
#     # Here, we assume that larger DBH increases competition (example factor: sqrt(DBH/10))
#     growth_competition_factor = math.sqrt(dbh / 10)
    
#     # Normalize by max_density to keep value between 0 and 1
#     density_factor = min((expected_trees_in_area * growth_competition_factor) / max_density, 1.0)

#     # Return the competition index
#     return round(density_factor, 2)

# fac=calculate_uniform_competition_index(6.36, 5, 20)
# print(fac)


