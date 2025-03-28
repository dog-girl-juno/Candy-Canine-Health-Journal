import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Fetch data from the database
def fetch_data():
    conn = sqlite3.connect("health_data.db")
    query = """
        SELECT date, hr, o2_sat, bp, pain, mood, nas, gi_symptoms, 
               body_temperature, fluid_intake, exercise_levels, 
               head, skin_symptoms, respiratory_symptoms 
        FROM health_data ORDER BY time ASC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Convert date to datetime format
    df["date"] = pd.to_datetime(df["date"])

    # Split blood pressure into systolic/diastolic (if stored as "120/80" format)
    df[["systolic_bp", "diastolic_bp"]] = df["bp"].str.split("/", expand=True).astype(float)

    return df

# Generate graph
def generate_graph():
    df = fetch_data()

    if df.empty:
        print("No data found in database.")
        return

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df["date"], df["hr"], marker="o", linestyle="-", label="Heart Rate (bpm)", color="red")
    ax.plot(df["date"], df["o2_sat"], marker="s", linestyle="--", label="Oxygen Saturation (%)", color="blue")
    ax.plot(df["date"], df["systolic_bp"], marker="^", linestyle="-.", label="Systolic BP", color="magenta")
    ax.plot(df["date"], df["diastolic_bp"], marker="v", linestyle=":", label="Diastolic BP", color="cyan")
    ax.plot(df["date"], df["pain"], marker="D", linestyle="-", label="Pain (1-10)", color="purple")
    ax.plot(df["date"], df["mood"], marker="X", linestyle="-", label="Mood (1-10)", color="green")
    ax.plot(df["date"], df["nas"], marker="P", linestyle="--", label="NAS (1-10)", color="orange")
    ax.plot(df["date"], df["gi_symptoms"], marker="x", linestyle="-.", label="GI Symptoms (1-10)", color="brown")
    ax.plot(df["date"], df["body_temperature"], marker="h", linestyle="--", label="Body Temperature (°C)", color="pink")
    ax.plot(df["date"], df["fluid_intake"], marker="*", linestyle=":", label="Fluid Intake (mL)", color="teal")

    # Format x-axis to display dates properly
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Labels & Title
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.title("Health Data Trends Over Time")

    # Show legend
    plt.legend()

    # Show grid for better readability
    plt.grid(True)

    # Display the graph
    plt.show()

# Run the graph function when script is executed
if __name__ == "__main__":
    generate_graph()
