def eco_suggestions(phone_minutes, laptop_minutes, tv_minutes):
    suggestions = []

    # Suggestions based on usage thresholds
    if phone_minutes > 60:
        suggestions.append("📱 Try reducing phone screen time to save energy.")
    if laptop_minutes > 120:
        suggestions.append("💻 Turn off your laptop when not in use.")
    if tv_minutes > 90:
        suggestions.append("📺 Consider reducing TV viewing to lower emissions.")

    # More general advice
    if phone_minutes + laptop_minutes + tv_minutes > 300:
        suggestions.append(
            "🌍 Consider minimizing screen time to save energy and reduce CO2."
        )

    return suggestions


# Define the number of minutes for phone, laptop, and TV usage
phone_minutes = 120  # Example value for phone usage
laptop_minutes = 180  # Example value for laptop usage
tv_minutes = 100  # Example value for TV usage

# Example of calling the suggestions engine
suggestions_list = eco_suggestions(phone_minutes, laptop_minutes, tv_minutes)

# Print suggestions
for suggestion in suggestions_list:
    print(suggestion)
