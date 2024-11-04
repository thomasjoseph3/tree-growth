const TEAK_PROFILES = {
    teak: {
        growth_phases: [
            // Each phase has actual growth rates for height (mm/year), DBH (mm/year), and volume (m³/year)
            { start_age: 0, end_age: 10, height_growth: 2000, dbh_growth: 7.5, volume_growth: 0.04 }, // Phase 1
            { start_age: 10, end_age: 20, height_growth: 1200, dbh_growth: 5.0, volume_growth: 0.024 }, // Phase 2
            { start_age: 20, end_age: 30, height_growth: 800, dbh_growth: 3.0, volume_growth: 0.016 } // Phase 3
        ],
        max_values: {
            max_height: 30.0,           // in meters
            max_canopy_diameter: 15.0,  // in meters, affects max DBH
            max_biomass: 1500.0         // in kg, or approx. 1.5 cubic meters for mature trees
        },
        temperature_tolerance: {
            optimal_range: { min: 21, max: 32 }, // in °C, ideal growth range
            cold_tolerance: 5,                  // minimum temperature in °C teak can tolerate
            heat_tolerance: 45                  // maximum temperature in °C teak can tolerate
        }
    }
}
