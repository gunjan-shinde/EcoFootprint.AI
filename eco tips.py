import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined appliance list and associated eco tips
appliance_tips = {
    "Air Conditioner": [
        "Set your thermostat to 24°C to reduce energy use.",
        "Clean AC filters monthly to increase efficiency.",
        "Use ceiling fans to reduce AC runtime.",
    ],
    "Refrigerator": [
        "Keep fridge temperature between 3°C and 5°C.",
        "Avoid overpacking to maintain airflow.",
        "Defrost freezer regularly to save energy.",
    ],
    "LED Bulbs": [
        "Switch to LED bulbs to reduce energy by up to 80%.",
        "Turn off lights when not needed.",
        "Use daylight where possible instead of artificial lights.",
    ],
    "Television": [
        "Turn off the TV completely instead of standby mode.",
        "Lower screen brightness to save power.",
    ],
    "Electric Vehicle": [
        "Charge during off-peak hours to reduce grid stress.",
        "Plan trips to optimize routes and reduce consumption.",
    ],
    "Washing Machine": [
        "Use cold water wash settings.",
        "Run full loads to reduce cycles.",
    ],
}

# All appliances and their textual descriptions (can be expanded)
appliance_descriptions = {
    "Air Conditioner": "cooling appliance used to lower temperature",
    "Refrigerator": "appliance to keep food cold",
    "LED Bulbs": "low energy lighting device",
    "Television": "entertainment appliance using electricity",
    "Electric Vehicle": "eco transport using electricity",
    "Washing Machine": "appliance to wash clothes",
}

# Combine descriptions into corpus for similarity matching
appliance_names = list(appliance_descriptions.keys())
descriptions = list(appliance_descriptions.values())

# Vectorizer setup
vectorizer = TfidfVectorizer()
description_vectors = vectorizer.fit_transform(descriptions)


# 🔍 Main Recommender Function
def recommend_eco_tips(user_appliances, top_n=5):
    tips = []
    for appliance in user_appliances:
        if appliance not in appliance_descriptions:
            continue
        # Get vector for user's appliance
        query = appliance_descriptions[appliance]
        query_vector = vectorizer.transform([query])
        similarity = cosine_similarity(query_vector, description_vectors)

        # Get top matches
        top_indices = similarity[0].argsort()[::-1][:top_n]
        for idx in top_indices:
            matched_appliance = appliance_names[idx]
            tips.extend(appliance_tips.get(matched_appliance, []))

    # Remove duplicates
    tips = list(set(tips))
    return tips[:top_n]


# 🎯 Example Usage
if __name__ == "__main__":
    user_appliances = ["Air Conditioner", "Refrigerator", "LED Bulbs"]
    print("📘 Recommended Eco Tips based on your usage:\n")
    recommendations = recommend_eco_tips(user_appliances)
    for i, tip in enumerate(recommendations, 1):
        print(f"{i}. {tip}")
