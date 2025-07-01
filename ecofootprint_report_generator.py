import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def generate_pdf_report(phone_emission, laptop_emission, tv_emission, total_emission, badge):
    # Define PDF save path to Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    pdf_path = os.path.join(desktop_path, "EcoFootprint_Report.pdf")

    # Create Pie Chart
    labels = ['Phone', 'Laptop', 'TV']
    sizes = [phone_emission, laptop_emission, tv_emission]
    colors = ['green', 'blue', 'orange']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("CO2 Emission Breakdown")
    pie_chart_path = os.path.join(desktop_path, "emission_pie_chart.png")
    plt.savefig(pie_chart_path)
    plt.close()

    # Create Bar Chart
    plt.figure(figsize=(6, 3))
    devices = ['Phone', 'Laptop', 'TV']
    emissions = [phone_emission, laptop_emission, tv_emission]
    bar_colors = ['blue', 'orange', 'purple']
    plt.barh(devices, emissions, color=bar_colors)
    plt.xlabel("CO2 Emission (g)")
    plt.title("Device-wise CO2 Emissions")
    bar_chart_path = os.path.join(desktop_path, "emission_bar_chart.png")
    plt.savefig(bar_chart_path)
    plt.close()

    # Generate PDF Report
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_fill_color(34, 139, 34)  # green
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 15, "EcoFootprint.AI Emission Report", ln=True, fill=True, align='C')

    # Emission values
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Phone: {phone_emission:.2f} g CO2", ln=True)
    pdf.cell(0, 10, f"Laptop: {laptop_emission:.2f} g CO2", ln=True)
    pdf.cell(0, 10, f"TV: {tv_emission:.2f} g CO2", ln=True)
    pdf.set_text_color(255, 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Total Emission: {total_emission:.2f} g CO2", ln=True)

    # Badge
    pdf.ln(5)
    pdf.set_text_color(0, 128, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Eco Badge: {badge}", ln=True)

    # Insert charts
    pdf.image(bar_chart_path, x=30, y=None, w=150)
    pdf.ln(10)
    pdf.image(pie_chart_path, x=30, y=None, w=150)

    # Save PDF
    pdf.output(pdf_path)

    print(f"✅ Report successfully saved on Desktop at: {pdf_path}")
