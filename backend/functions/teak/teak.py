TREE_PROFILES = {
    "teak": {
        "growth_phases": [
            # Early Phase: Rapid growth in height and DBH, moderate volume growth
            { 
                "start_age": 0, 
                "end_age": 10, 
                "height_growth": 1000,       # mm/year, slightly reduced
                "dbh_growth": 1.8,           # cm/year, realistic early phase rate
                "volume_growth": 0.03        # m³/year, more conservative early volume growth
            },
            
            # Middle Phase: Slower height growth, steady DBH growth, increased volume growth as tree matures
            { 
                "start_age": 10, 
                "end_age": 20, 
                "height_growth": 700,        # mm/year, moderate height increment
                "dbh_growth": 1.3,           # cm/year, realistic middle phase rate
                "volume_growth": 0.035       # m³/year, slight increase in volume growth
            },
            
            # Late Phase: Minimal height growth, reduced DBH growth, lower volume growth as tree stabilizes
            { 
                "start_age": 20, 
                "end_age": 30, 
                "height_growth": 300,        # mm/year, minimal height growth
                "dbh_growth": 0.8,           # cm/year, realistic late phase rate
                "volume_growth": 0.015       # m³/year, as volume growth slows
            }
        ],
        "max_values": {
            "max_height": 35.0,             # meters, adjusted for typical plantation limit
            "max_canopy_diameter": 9.0,     # meters, realistic canopy range
            "max_biomass": 1300.0           # kg, realistic upper limit
        },
        "temperature_tolerance": {
            "cold_tolerance": 5,
            "heat_tolerance": 45
        }
    }
}
