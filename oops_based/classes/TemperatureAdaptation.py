# TemperatureAdaptation.py

class TemperatureAdaptation:
    def __init__(self, average_temp, tree):
        self.average_temp = average_temp
        self.optimal_temp_range = tree.temperature_tolerance.get("optimal_temp_range", (20, 30))  # Default values if not set
        self.cold_tolerance = tree.temperature_tolerance.get("cold_tolerance", 15)
        self.heat_tolerance = tree.temperature_tolerance.get("heat_tolerance", 38)

    def calculate(self):
        min_temp, max_temp = self.optimal_temp_range

        if min_temp <= self.average_temp <= max_temp:
            # Within optimal range, full adaptation
            adaptation_score = 1.0
        else:
            # Calculate deviation from the optimal range boundary
            deviation = min(abs(self.average_temp - min_temp), abs(self.average_temp - max_temp))

            # Adjust penalty based on cold and heat tolerance limits
            if self.average_temp < self.cold_tolerance:
                # Severe penalty if below cold tolerance
                adaptation_score = max(1 - (deviation / 10), 0)
            elif self.average_temp > self.heat_tolerance:
                # Severe penalty if above heat tolerance
                adaptation_score = max(1 - (deviation / 10), 0)
            else:
                # Moderate penalty for temperatures outside optimal range but within tolerance
                if deviation > 10:
                    # Strong penalty for deviations greater than 10 degrees
                    adaptation_score = max(1 - (deviation / 5), 0)
                else:
                    # Mild penalty for smaller deviations within 10 degrees
                    adaptation_score = max(1 - (deviation / 10), 0)

        return round(adaptation_score, 2)
