# Corrected species-specific growth parameters for teak
TEAK_PROFILES =  {
    "teak": {
        "base_growth_rate": {
            "height": 4.0,  # mm/year for height growth
            "dbh": 3.0,     # mm/year for DBH growth
            "volume": 0.05  # m³/year for volume growth
        },
        "growth_phases": [
            # (start age, end age, height multiplier, dbh multiplier, volume multiplier)
            (0, 10, 1.2, 1.1, 1.2),  # Phase 1
            (10, 20, 0.8, 0.7, 0.8),  # Phase 2
            (20, 30, 0.6, 0.5, 0.6)   # Phase 3
        ],
        "max_height": 30.0,  # meters
        "max_canopy_diameter": 15.0,  # meters
        "max_biomass": 1500.0,  # kg
        "temperature_tolerance": {
            "cold_tolerance": 5,   # Minimum temperature in °C teak can tolerate
            "heat_tolerance": 45   # Maximum temperature in °C teak can tolerate
        }
    }
}
