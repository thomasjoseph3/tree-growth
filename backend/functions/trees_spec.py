TREE_PROFILES = {
    "teak": {
        "growth_phases": [
            # Early Phase: Rapid growth in height and DBH, moderate volume growth
            { 
                "start_age": 0, 
                "end_age": 10, 
                "height_growth": 1000,       # mm/year
                "dbh_growth": 1.8,           # cm/year
                "volume_growth": 0.03        # m³/year
            },
            # Middle Phase
            { 
                "start_age": 10, 
                "end_age": 20, 
                "height_growth": 700,        # mm/year
                "dbh_growth": 1.3,           # cm/year
                "volume_growth": 0.035       # m³/year
            },
            # Late Phase
            { 
                "start_age": 20, 
                "end_age": 30, 
                "height_growth": 300,        # mm/year
                "dbh_growth": 0.8,           # cm/year
                "volume_growth": 0.015       # m³/year
            }
        ],
        "max_values": {
            "max_height": 35.0,             # meters
            "max_canopy_diameter": 9.0,     # meters
            "max_biomass": 1300.0           # kg
        },
        "temperature_tolerance": {
            "cold_tolerance": 5,
            "heat_tolerance": 45
        }
    },
    "pine": {
        "growth_phases": [
            # Early Phase
            { 
                "start_age": 0, 
                "end_age": 10, 
                "height_growth": 800,        # mm/year
                "dbh_growth": 1.5,           # cm/year
                "volume_growth": 0.025       # m³/year
            },
            # Middle Phase
            { 
                "start_age": 10, 
                "end_age": 20, 
                "height_growth": 500,        # mm/year
                "dbh_growth": 1.2,           # cm/year
                "volume_growth": 0.03        # m³/year
            },
            # Late Phase
            { 
                "start_age": 20, 
                "end_age": 40, 
                "height_growth": 200,        # mm/year
                "dbh_growth": 0.7,           # cm/year
                "volume_growth": 0.02        # m³/year
            }
        ],
        "max_values": {
            "max_height": 30.0,             # meters
            "max_canopy_diameter": 8.0,     # meters
            "max_biomass": 1000.0           # kg
        },
        "temperature_tolerance": {
            "cold_tolerance": -10,
            "heat_tolerance": 40
        }
    },
    "eucalyptus": {
        "growth_phases": [
            # Early Phase
            { 
                "start_age": 0, 
                "end_age": 10, 
                "height_growth": 1200,       # mm/year
                "dbh_growth": 2.0,           # cm/year
                "volume_growth": 0.04        # m³/year
            },
            # Middle Phase
            { 
                "start_age": 10, 
                "end_age": 20, 
                "height_growth": 800,        # mm/year
                "dbh_growth": 1.5,           # cm/year
                "volume_growth": 0.05        # m³/year
            },
            # Late Phase
            { 
                "start_age": 20, 
                "end_age": 30, 
                "height_growth": 300,        # mm/year
                "dbh_growth": 1.0,           # cm/year
                "volume_growth": 0.03        # m³/year
            }
        ],
        "max_values": {
            "max_height": 40.0,             # meters
            "max_canopy_diameter": 10.0,    # meters
            "max_biomass": 1500.0           # kg
        },
        "temperature_tolerance": {
            "cold_tolerance": 0,
            "heat_tolerance": 50
        }
    }
}
