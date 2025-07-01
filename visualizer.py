import matplotlib.pyplot as plt

# Function to display Pie Chart of CO2 breakdown
def show_pie_chart():
    labels = ['YouTube', 'Zoom', 'Email', 'Instagram', 'Netflix']
    sizes = [25, 20, 15, 30, 10]  # Replace with actual data
    explode = (0.1, 0, 0, 0, 0)  # Highlight the first slice
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title("CO₂ Emission Breakdown by Activity")
    plt.show()

# Function to display Bar Chart for CO2 comparison over weeks
def show_bar_chart():
    activities = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
    emissions = [150, 200, 180, 220, 250]  # Replace with actual weekly emission data
    plt.bar(activities, emissions, color='green')
    plt.xlabel('Weeks')
    plt.ylabel('CO₂ Emissions (grams)')
    plt.title('Weekly CO₂ Emissions Comparison')
    plt.show()

# Function to display Gauge Chart for eco-status
def show_gauge_chart():
    import plotly.graph_objects as go

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=45,  # Replace with actual emission value
        title={'text': "Eco Status"},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75, 'value': 60}}))

    fig.show()

