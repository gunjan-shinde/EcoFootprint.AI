import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

# Path to store historical data
HISTORY_FILE = "carbon_history.csv"


# Function to save daily CO2 report
def save_daily_report(electricity_kg, transport_kg, diet_kg, total_kg=None):
    date = datetime.date.today().isoformat()
    total_kg = (
        total_kg if total_kg is not None else electricity_kg + transport_kg + diet_kg
    )

    data = {
        "date": date,
        "electricity_kg": electricity_kg,
        "transport_kg": transport_kg,
        "diet_kg": diet_kg,
        "total_kg": total_kg,
    }

    df = pd.DataFrame([data])

    if os.path.exists(HISTORY_FILE):
        df.to_csv(HISTORY_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(HISTORY_FILE, index=False)

    print(f"✅ Report saved for {date}")


# Function to compare past reports
def compare_reports():
    if not os.path.exists(HISTORY_FILE):
        print("❌ No history found.")
        return

    df = pd.read_csv(HISTORY_FILE)
    df["date"] = pd.to_datetime(df["date"])

    print("\n📅 Past Carbon Emission Reports:")
    print(df.sort_values("date", ascending=False).to_string(index=False))

    # Plot bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(df["date"].dt.strftime("%Y-%m-%d"), df["total_kg"], color="#2E8B57")
    plt.title("Daily Total Carbon Emissions")
    plt.xlabel("Date")
    plt.ylabel("Total CO₂ Emitted (kg)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis="y")
    plt.show()
