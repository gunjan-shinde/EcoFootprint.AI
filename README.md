## EcoFootprint.AI ##

EcoFootprint.AI is an AI-powered Streamlit web application designed to help users **predict, track, visualize, and reduce their digital carbon footprint**. By analyzing activities like streaming, video calls, and email usage, the app calculates estimated CO₂ emissions and offers **smart eco-friendly suggestions, gamification badges, and interactive visualizations** to encourage a greener digital lifestyle.

# Key Features

- Live Carbon Emission Calculator
   Input usage of platforms like YouTube, Zoom, Gmail, etc.
   Real-time CO₂ estimation based on scientifically-backed emission factors.

- Save & Compare History
   Save daily/weekly usage and track environmental impact over time.
   View comparisons between past and present emissions.

- Dynamic Visualizations
   Interactive line charts, bar graphs, and pie charts.
   Trend analysis and footprint breakdown by category.

- Gamification & Eco Badges
   Get rewarded with digital eco-badges for eco-friendly behavior.
   Avatar reactions change based on your performance (happy, neutral, sad).

- ML-Based Suggestions Engine
   Recommends personalized eco-tips using a trained machine learning model.
   Learns from your habits to suggest optimal changes.

- "What If" Simulator
   Simulate the impact of behavior changes (e.g., reducing Zoom hours).
   Compare actual vs hypothetical CO₂ output.

- Downloadable Eco Report Card (PDF)
   Generate and download a customized sustainability report.
  Includes tips, badges, charts, and historical summary.


# Tech Stack

 Layer                                           Tools Used                                  

Frontend                                          Streamlit                                   
Backend                                     Python, Pandas, NumPy                       
Visualization                             Plotly, Matplotlib, Seaborn                 
ML & Suggestions                               Scikit-learn, NLTK                         
PDF Report                                      ReportLab, FPDF                             
AR/Avatar                                  OpenCV, Image Processing                    
Storage                              Local file system or SQLite (optional)      


# Project Structure
EcoFootprint.AI/
├── main.py # Main Streamlit app UI
├── carbon_emission_calculator.py # CO₂ calculation logic
├── suggestions_engine.py # ML-based eco tips recommender
├── visualization.py # Dynamic charts and graphs
├── avatar_display.py # Avatar expressions based on emission
├── report_generator.py # PDF report card generator
├── what_if_simulator.py # What-If behavior impact calculator
├── history_manager.py # Save and compare emission history
├── assets/
│ ├── happy.png
│ ├── neutral.png
│ └── sad.png
├── data/
│ └── usage_history.csv # Stored emission data
├── requirements.txt # List of Python dependencies
└── README.md # Project description
