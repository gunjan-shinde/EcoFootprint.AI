import os
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Emission factors in g/min
EMISSION_FACTORS = {"phone": 1.5, "laptop": 3.2, "tv": 2.5}


# Direct emission calculation
def calculate_emission(phone, laptop, tv):
    return round(
        phone * EMISSION_FACTORS["phone"]
        + laptop * EMISSION_FACTORS["laptop"]
        + tv * EMISSION_FACTORS["tv"],
        2,
    )


# Avatar display
def show_avatar(emission, title):
    if emission <= 600:
        avatar_path = "C:/Users/Gunjan/Downloads/happy.png"
    elif emission <= 1200:
        avatar_path = "C:/Users/Gunjan/Downloads/neutral.png"
    else:
        avatar_path = "C:/Users/Gunjan/Downloads/sad.png"

    window = tk.Tk()
    window.title(title)
    img = Image.open(avatar_path)
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack(padx=20, pady=20)

    tk.Label(
        window, text=f"{title}\nYour CO₂: {emission} g/day", font=("Arial", 14)
    ).pack(pady=10)
    tk.Button(window, text="Close", command=window.destroy).pack(pady=10)
    window.mainloop()


# Pie chart
def generate_pie_chart(phone, laptop, tv):
    values = [
        phone * EMISSION_FACTORS["phone"],
        laptop * EMISSION_FACTORS["laptop"],
        tv * EMISSION_FACTORS["tv"],
    ]
    labels = ["Phone", "Laptop", "TV"]
    colors = ["#77dd77", "#84b6f4", "#ffb347"]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", colors=colors)
    ax.set_title("CO₂ Emission Breakdown")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode()


# HTML report
def generate_html_report(
    file_path,
    title,
    phone,
    laptop,
    tv,
    emission,
    actual_emission=None,
    include_badges=False,
    is_comparison=False,
):
    pie_chart = generate_pie_chart(phone, laptop, tv)

    badge_html = ""
    tips_html = ""
    comparison_html = ""

    if include_badges and actual_emission:
        reduction = actual_emission - emission
        reduction_percent = (reduction / actual_emission) * 100

        if reduction_percent >= 20:
            badge_html = f"<div class='badge'>🏅 Eco Hero! You reduced emissions by {reduction_percent:.1f}%!</div>"
            tips_html = """
                <div class='tip'>🌱 Tip: Use power-saving mode on all devices.</div>
                <div class='tip'>🚶‍♀️ Tip: Try a screen-free hour daily for lower emissions.</div>
                <div class='tip'>🔌 Tip: Turn off devices when not in use to avoid phantom load.</div>
            """
        else:
            badge_html = "<div class='badge' style='background-color:#f8d7da; color:#721c24;'>📉 Reduction under 20%. Keep trying!</div>"

        if is_comparison:
            comparison_html = f"""
            <div style="margin-top:20px;">
                <h3>📊 Comparison Summary:</h3>
                <p>🟢 <b>Actual Emission:</b> {actual_emission} g/day</p>
                <p>🟡 <b>Hypothetical Emission:</b> {emission} g/day</p>
                <p>📉 <b>Emission Reduced:</b> {reduction:.2f} g/day ({reduction_percent:.1f}%)</p>
            </div>
            """

    html_content = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                padding: 20px;
                background-color: #f0fff0;
                color: #333;
            }}
            h1 {{ color: #2e8b57; }}
            .badge {{
                background-color: #d4edda;
                color: #155724;
                padding: 12px;
                border-radius: 8px;
                margin: 15px 0;
            }}
            .tip {{
                background-color: #fff3cd;
                color: #856404;
                padding: 10px;
                border-radius: 6px;
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <p><strong>📱 Phone Usage:</strong> {phone} minutes/day</p>
        <p><strong>💻 Laptop Usage:</strong> {laptop} minutes/day</p>
        <p><strong>📺 TV Usage:</strong> {tv} minutes/day</p>
        <h2>🌍 CO₂ Emission: {emission} g/day</h2>
        <img src="data:image/png;base64,{pie_chart}" alt="Pie Chart" style="max-width: 400px; margin-top: 20px;"/>
        {comparison_html}
        {badge_html}
        {tips_html}
    </body>
    </html>
    """

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    webbrowser.open(f"file://{os.path.realpath(file_path)}")


# Main logic
def main():
    print("🌿 Welcome to EcoFootprint.AI")

    # Actual usage
    phone = int(input("📱 Enter actual phone usage (in minutes/day): "))
    laptop = int(input("💻 Enter actual laptop usage (in minutes/day): "))
    tv = int(input("📺 Enter actual TV usage (in minutes/day): "))

    actual_emission = calculate_emission(phone, laptop, tv)
    actual_path = "C:/Users/Gunjan/Desktop/EcoFootprint_Report_Actual.html"
    generate_html_report(
        actual_path, "Actual Usage Report", phone, laptop, tv, actual_emission
    )
    show_avatar(actual_emission, "Actual Usage Avatar")
    print(f"✅ Report successfully generated at: {actual_path}")

    # Hypothetical
    print("\n--- 🔮 What If Simulator ---")
    h_phone = int(input("📱 Hypothetical phone usage (minutes/day): "))
    h_laptop = int(input("💻 Hypothetical laptop usage (minutes/day): "))
    h_tv = int(input("📺 Hypothetical TV usage (minutes/day): "))

    hypo_emission = calculate_emission(h_phone, h_laptop, h_tv)
    hypo_path = "C:/Users/Gunjan/Desktop/EcoFootprint_Report_Hypothetical.html"
    generate_html_report(
        hypo_path, "Hypothetical Usage Report", h_phone, h_laptop, h_tv, hypo_emission
    )
    show_avatar(hypo_emission, "Hypothetical Avatar")
    print(f"✅ Hypothetical report saved to: {hypo_path}")

    # Comparison
    comp_path = "C:/Users/Gunjan/Desktop/EcoFootprint_Report_Comparison.html"
    generate_html_report(
        comp_path,
        "Comparison Report",
        h_phone,
        h_laptop,
        h_tv,
        hypo_emission,
        actual_emission=actual_emission,
        include_badges=True,
        is_comparison=True,
    )
    print(f"✅ Comparison Report with tips & badge saved to: {comp_path}")


if __name__ == "__main__":
    main()
