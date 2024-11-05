TREE_PROFILES = {
    "teak": {
        "growth_phases": [
            # Early Phase: Rapid growth in height and DBH, moderate volume growth
            { "start_age": 0, "end_age": 10, "height_growth": 1200, "dbh_growth": 6.0, "volume_growth": 0.035 },
            
            # Middle Phase: Slower height growth, steady DBH growth, increased volume growth as tree matures
            { "start_age": 10, "end_age": 20, "height_growth": 800, "dbh_growth": 4.5, "volume_growth": 0.03 },
            
            # Late Phase: Minimal height growth, reduced DBH growth, lower volume growth as tree stabilizes
            { "start_age": 20, "end_age": 30, "height_growth": 200, "dbh_growth": 2.5, "volume_growth": 0.015 }
        ],
        "max_values": {
            "max_height": 46.0,             # meters
            "max_canopy_diameter": 9.8,    # meters, affects max DBH
            "max_biomass": 1500.0           # kg
        },
        "temperature_tolerance": {
            "cold_tolerance": 5,
            "heat_tolerance": 45
        }
    }
}
