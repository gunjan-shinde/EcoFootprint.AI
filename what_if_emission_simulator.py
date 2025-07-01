# Function to calculate emissions based on screen time (in minutes)
def calculate_emission(phone_minutes, laptop_minutes, tv_minutes):
    # Simple emission calculation (just an example)
    phone_emission = phone_minutes * 0.1  # Example: 0.1 grams CO2 per minute for phone
    laptop_emission = (
        laptop_minutes * 0.2
    )  # Example: 0.2 grams CO2 per minute for laptop
    tv_emission = tv_minutes * 0.3  # Example: 0.3 grams CO2 per minute for TV
    total_emission = phone_emission + laptop_emission + tv_emission
    return total_emission


# What If Simulator function to simulate the effect of reducing screen time
def what_if_simulator(
    phone_minutes, laptop_minutes, tv_minutes, change_type, change_value
):
    if change_type == "phone":
        phone_minutes -= change_value
    elif change_type == "laptop":
        laptop_minutes -= change_value
    elif change_type == "tv":
        tv_minutes -= change_value

    # Recalculate emissions with new values
    total_emission = calculate_emission(phone_minutes, laptop_minutes, tv_minutes)
    print(f"🌍 After reducing {change_value} minutes of {change_type}:")
    print(f"Your new total carbon emission is: {total_emission:.2f} grams CO2")


# Define initial device usage in minutes
phone_minutes = 120  # Example value for phone usage
laptop_minutes = 180  # Example value for laptop usage
tv_minutes = 100  # Example value for TV usage

# Get user input for the "What If" scenario
change_type = input("Enter device (phone, laptop, tv): ").strip().lower()
change_value = float(input(f"How many minutes to reduce from {change_type}: "))

# Call the what_if_simulator to simulate the change and display results
what_if_simulator(phone_minutes, laptop_minutes, tv_minutes, change_type, change_value)
