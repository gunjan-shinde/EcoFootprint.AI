def calculate_daily_co2(electricity_kwh, transport_km, diet_type):
    # Emission factors (in kg CO2)
    electricity_emission_factor = 0.475   # per kWh
    transport_emission_factor = 0.21      # per km

    # Diet emission based on type
    diet_emission = {
        "meat-heavy": 5.0,
        "vegetarian": 3.0,
        "vegan": 2.0
    }

    # Calculate emissions
    elec_emission = electricity_kwh * electricity_emission_factor
    trans_emission = transport_km * transport_emission_factor
    diet_emission_val = diet_emission.get(diet_type.lower(), 5.0)  # Default to meat-heavy

    total_emission = round(elec_emission + trans_emission + diet_emission_val, 2)
    return total_emission

if __name__ == "__main__":
    print("🌍 Daily Carbon Emission Calculator")

    try:
        electricity = float(input("🔌 Enter electricity used today (in kWh): "))
        transport = float(input("🚗 Enter distance travelled today (in km): "))
        diet = input("🍽️ Enter your diet type (meat-heavy / vegetarian / vegan): ")

        total_co2 = calculate_daily_co2(electricity, transport, diet)

        print(f"\n📦 Your estimated CO₂ emission for today: {total_co2} kg")
    except Exception as e:
        print("❌ Invalid input. Please try again.")
        print("Error:", e)
