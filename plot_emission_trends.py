import matplotlib.pyplot as plt
import pandas as pd


# Function to plot daily and weekly CO2 trends
def plot_daily_weekly_trends():
    try:
        # Load the emission data from CSV
        df = pd.read_csv("daily_emissions.csv")

        # Check if required columns are present
        required_columns = ["Date", "Total Emission (g CO2)"]
        if not all(col in df.columns for col in required_columns):
            print(f"Missing required columns in data")
            return

        # Convert 'Date' to datetime
        df["Date"] = pd.to_datetime(df["Date"])

        # Set 'Date' as the index for easier manipulation
        df.set_index("Date", inplace=True)

        # Resample by day for daily data
        daily_data = df["Total Emission (g CO2)"].resample("D").sum()

        # Resample by week for weekly data
        weekly_data = df["Total Emission (g CO2)"].resample("W").sum()

        # Plotting
        plt.figure(figsize=(12, 6))

        # Daily emissions plot
        plt.subplot(1, 2, 1)
        plt.plot(
            daily_data.index,
            daily_data.values,
            label="Daily CO2 Emissions",
            color="blue",
            marker="o",
        )
        plt.title("Daily CO2 Emissions")
        plt.xlabel("Date")
        plt.ylabel("Emissions (g CO2)")
        plt.xticks(rotation=45)
        plt.grid(True)

        # Weekly emissions plot
        plt.subplot(1, 2, 2)
        plt.plot(
            weekly_data.index,
            weekly_data.values,
            label="Weekly CO2 Emissions",
            color="red",
            marker="o",
        )
        plt.title("Weekly CO2 Emissions")
        plt.xlabel("Week")
        plt.ylabel("Emissions (g CO2)")
        plt.xticks(rotation=45)
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error while plotting trends: {e}")


# Call this function after saving emission data to display the charts
plot_daily_weekly_trends()
