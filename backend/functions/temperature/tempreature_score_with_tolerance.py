def calculate_temperature_adaptation(average_temp, optimal_temp_range, cold_tolerance, heat_tolerance):
    min_temp, max_temp = optimal_temp_range
    
    if min_temp <= average_temp <= max_temp:
        # Within optimal range, full adaptation
        adaptation_score = 1.0
    else:
        # Calculate deviation from the optimal range boundary
        deviation = min(abs(average_temp - min_temp), abs(average_temp - max_temp))
        
        # Adjust penalty based on cold and heat tolerance limits
        if average_temp < cold_tolerance:
            # Severe penalty if below cold tolerance
            adaptation_score = max(1 - (deviation / 10), 0)  # Adjust divisor based on tolerance strength
        elif average_temp > heat_tolerance:
            # Severe penalty if above heat tolerance
            adaptation_score = max(1 - (deviation / 10), 0)
        else:
            # Moderate penalty for temperatures outside optimal range but within tolerance
            if deviation > 10:
                # Strong penalty for deviations greater than 10 degrees from optimal
                adaptation_score = max(1 - (deviation / 5), 0)
            else:
                # Mild penalty for smaller deviations within 10 degrees
                adaptation_score = max(1 - (deviation / 10), 0)

    return round(adaptation_score, 2)

# # Example usage
# optimal_temp_range = (20, 30)    # Teak tree optimal range
# cold_tolerance = 15              # Minimum temperature teak can tolerate
# heat_tolerance = 38              # Maximum temperature teak can tolerate
# average_temp = 33                # Example temperature

# adaptation_score = calculate_temperature_adaptation(
#     average_temp, optimal_temp_range, cold_tolerance, heat_tolerance
# )
# print("Temperature Adaptation Score:", adaptation_score)
