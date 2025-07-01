import pandas as pd
import plotly.graph_objects as go


def dynamic_visualization():
    try:
        # Load the emission data from CSV
        df = pd.read_csv("daily_emissions.csv")

        # Convert 'Date' to datetime for proper plotting
        df["Date"] = pd.to_datetime(df["Date"])

        # Plotly interactive plot for daily emissions
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["Phone Emission (g CO2)"],
                mode="lines+markers",
                name="Phone Emissions",
                line=dict(color="red"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["Laptop Emission (g CO2)"],
                mode="lines+markers",
                name="Laptop Emissions",
                line=dict(color="green"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["TV Emission (g CO2)"],
                mode="lines+markers",
                name="TV Emissions",
                line=dict(color="blue"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["Total Emission (g CO2)"],
                mode="lines+markers",
                name="Total Emissions",
                line=dict(color="orange"),
            )
        )

        fig.update_layout(
            title="Interactive CO₂ Emissions Over Time",
            xaxis_title="Date",
            yaxis_title="Emissions (g CO2)",
            template="plotly_dark",
        )

        # Show the plot
        fig.show()

        # Save the plot as an HTML file
        fig.write_html("interactive_emissions_plot.html")
        print("Plot saved as interactive_emissions_plot.html")

    except Exception as e:
        print(f"Error in dynamic visualization: {e}")


# Call dynamic_visualization() after data is saved
dynamic_visualization()
