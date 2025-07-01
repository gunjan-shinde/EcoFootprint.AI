# emissions.py


def calculate_emission(device_hours=2, co2_per_hour=0.5):
    """
    Calculates CO2 emission based on device usage in hours.
    """
    total_emission = device_hours * co2_per_hour
    return total_emission
