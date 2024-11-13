import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_spec import TREE_PROFILES
from Tree import Tree
from SoilQuality import SoilQuality
from TreeSimulation import TreeSimulation
from WaterAvailability import WaterAvailability
from TemperatureAdaptation import TemperatureAdaptation
from CompetitionIndex import CompetitionIndex
# Sample data from TREE_PROFILES
teak_tree = Tree("teak", TREE_PROFILES["teak"])

soil_quality = SoilQuality(
    soil_type="loamy",
    pH=6.5,
    nitrogen=75,
    phosphorus=35,
    potassium=40,
    organic_matter=28
)
water_availability = WaterAvailability(
    annual_rainfall=1500, 
    soil_type="loamy", 
    drainage="well_drained", 
    tree=teak_tree 
)

temperature_adaptation = TemperatureAdaptation(
    average_temp=33,
    tree=teak_tree
)

competition_index = CompetitionIndex(
    tree_spacing=3.0,
    influence_radius=2.5,
    dbh=30,
    crown_diameter=4.0
)



simulation = TreeSimulation(teak_tree, soil_quality,water_availability,temperature_adaptation,competition_index)
simulation.run()
