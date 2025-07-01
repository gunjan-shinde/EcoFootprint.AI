# carbon_emission_calculator.py
def calculate_carbon_emission(minutes, device):
    emission_factors = {
        'phone': 0.1,  # Emission factor per minute for phone usage (grams CO2)
        'laptop': 0.2,  # Emission factor per minute for laptop usage (grams CO2)
        'tv': 0.25  # Emission factor per minute for TV usage (grams CO2)
    }

    return minutes * emission_factors.get(device, 0)
