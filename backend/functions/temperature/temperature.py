def calculate_temperature_adaptation(average_temp, optimal_temp_range):
    min_temp, max_temp = optimal_temp_range
    if min_temp <= average_temp <= max_temp:
        # Within optimal range, full adaptation
        adaptation_score = 1.0
    else:
        # Calculate deviation from the nearest bound of the optimal range
        deviation = min(abs(average_temp - min_temp), abs(average_temp - max_temp))
        
        # Apply a sharper penalty for large deviations
        if deviation > 10:
            # Extreme penalty for temperatures 10 degrees or more outside the optimal range
            adaptation_score = max(1 - (deviation / 5), 0)
        else:
            # Mild penalty for deviations within 10 degrees
            adaptation_score = max(1 - (deviation / 10), 0)
    
    return round(adaptation_score, 2)

# # Example usage
# optimal_temp_range = (20, 30)  # Teak tree optimal range
# average_temp = 33 
# adaptation_score = calculate_temperature_adaptation(33, (20, 30))
# print("Temperature Adaptation Score:", adaptation_score)
