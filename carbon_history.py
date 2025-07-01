import json
import os
import datetime
import matplotlib.pyplot as plt

# Path to store reports
REPORTS_FILE = "emission_reports.json"


# Save daily report
def save_daily_report(electricity, transport, diet, total_emission):
    data = {
        "date": str(datetime.date.today()),
        "electricity": electricity,
        "transport": transport,
        "diet": diet,
        "total_emission": total_emission,
    }

    if os.path.exists(REPORTS_FILE):
        with open(REPORTS_FILE, "r") as file:
            reports = json.load(file)
    else:
        reports = []

    reports.append(data)

    with open(REPORTS_FILE, "w") as file:
        json.dump(reports, file, indent=4)


# Compare reports using a bar chart
def compare_reports():
    if not os.path.exists(REPORTS_FILE):
        print("No report history found.")
        return

    with open(REPORTS_FILE, "r") as file:
        reports = json.load(file)

    dates = [r["date"] for r in reports]
    emissions = [r["total_emission"] for r in reports]

    plt.figure(figsize=(10, 5))
    plt.bar(dates, emissions, color="green")
    plt.xlabel("Date")
    plt.ylabel("Total CO₂ Emissions (kg)")
    plt.title("Your Daily Carbon Emissions Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
