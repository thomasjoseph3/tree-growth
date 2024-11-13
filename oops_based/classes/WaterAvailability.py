class WaterAvailability:
    SOIL_RETENTION = {
        "loamy": 0.85,
        "sandy": 0.4,
        "clay": 0.75,
        "laterite": 0.6,
        "peaty": 0.9,
        "black cotton": 0.7,
        "alluvial": 0.8
    }

    DRAINAGE_RETENTION = {
        "well_drained": 0.9,
        "moderately_drained": 0.7,
        "poorly_drained": 0.5
    }

    def __init__(self, annual_rainfall, soil_type, drainage, tree):
        self.annual_rainfall = annual_rainfall
        self.soil_type = soil_type.lower()
        self.drainage = drainage.lower()
        self.tree = tree  

    def calculate(self):
        # Get soil and drainage retention factors
        soil_retention_factor = self.SOIL_RETENTION.get(self.soil_type, 0.5)  # Default to 0.5 if unknown
        drainage_retention_factor = self.DRAINAGE_RETENTION.get(self.drainage, 0.7)  # Default to 0.7 if unknown

        # Calculate Effective Water Availability (EWA) in mm
        ewa = self.annual_rainfall * soil_retention_factor * drainage_retention_factor

        # Access the water range directly from the Tree instance
        optimal_water_min, optimal_water_max = self.tree.water_range

        # Normalize water availability to a range of 0 to 1
        if ewa < optimal_water_min:
            # Apply penalty decay for insufficient water
            normalized_water_availability = (ewa / optimal_water_min) ** 0.5  # Square root decay
        elif ewa > optimal_water_max:
            # Apply penalty decay for excess water
            normalized_water_availability = (optimal_water_max / ewa) ** 0.5  # Square root decay
        else:
            # Within optimal range, scale linearly between min and max
            normalized_water_availability = (ewa - optimal_water_min) / (optimal_water_max - optimal_water_min)

        # Ensure the normalized value is between 0 and 1
        return round(min(max(normalized_water_availability, 0), 2), 2)
