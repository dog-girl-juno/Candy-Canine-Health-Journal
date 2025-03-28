import sqlite3
import time
from datetime import datetime
import os
import subprocess
from colorama import Fore, Back, Style, init

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_db():
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            time INTEGER,
            bp TEXT,
            hr INTEGER,
            o2_sat REAL,
            nas INTEGER,
            head INTEGER,
            pain INTEGER,
            mood INTEGER,
            body_position TEXT,
            body_temperature REAL,
            fluid_intake INTEGER,
            exercise_levels INTEGER,
            gi_symptoms INTEGER,
            skin_symptoms TEXT,
            respiratory_symptoms TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_user_input():
    print("\nEnter health data:")
    bp = input("Blood Pressure (SYS/DIA) [e.g., 120/80]: ") or ""
    hr = input("Heart Rate (bpm): ") or 0
    o2_sat = input("Oxygen Saturation (%): ") or 0.0
    nas = input("Nausea (1-10): ") or 0
    head = input("Headache (1-10): ") or 0
    pain = input("Joint Pain (1-10): ") or 0
    mood = input("Emotional State (1-10): ") or 0
    body_position = input("Body Position (Standing/Sitting/Lying): ") or ""
    body_temperature = input("Body Temperature (°C): ") or 0.0
    fluid_intake = input("Fluid Intake (mL): ") or 0
    exercise_levels = input("Exercise Levels (1-10): ") or 0
    gi_symptoms = input("GI Symptoms (1-10): ") or 0
    skin_symptoms = input("Skin Symptoms (Flushing/Rashes/Swelling/Normal): ") or ""
    respiratory_symptoms = input("Respiratory Symptoms (Shortness of Breath/Congestion/Wheezing/Normal): ") or ""
    notes = input("Notes: ") or ""

    return (bp, int(hr), float(o2_sat), int(nas), int(head), int(pain), int(mood),
            body_position, float(body_temperature), int(fluid_intake), int(exercise_levels),
            int(gi_symptoms), skin_symptoms, respiratory_symptoms, notes)

def insert_data():
    create_db()
    date = datetime.now().strftime("%Y-%m-%d")
    timestamp = int(time.time())
    data = get_user_input()
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO health_data (date, time, bp, hr, o2_sat, nas, head, pain, mood, 
                                body_position, body_temperature, fluid_intake, exercise_levels, 
                                gi_symptoms, skin_symptoms, respiratory_symptoms, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (date, timestamp) + data)
    conn.commit()
    conn.close()
    print("\nData successfully saved!")

def view_past_entries():
    create_db()
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_data ORDER BY time DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    print("\nRecent Entries:")
    print("="*50)
    for row in rows:
        print(f"Date: {row[1]}, Time: {datetime.fromtimestamp(row[2])}, BP: {row[3]}, HR: {row[4]}, O2 Sat {row[5]}, Nausua {row[6]}, Headache {row[7]}, Joint Pain {row[8]}, Mood {row[9]}, Position {row[10]}, Temp {row[11]}, Fluids {row[12]}, Activity {row[13]}, GI {row[14]}, Skin {row[15]}, Breathing {row[16]}")
    print("="*50)


def open_graph_script():
    try:
        subprocess.run(["python", "graph.py"], check=True)
    except FileNotFoundError:
        print("Error: graph.py not found!")
    except Exception as e:
        print(f"Error running graph.py: {e}")

def main_menu():
    while True:
        clear_screen()
        print(Fore.WHITE + "|", "="*51, "|")
        print(Fore.WHITE + "|", Style.BRIGHT + Fore.GREEN + "           Candy Canine Health Journal             ", Fore.WHITE + "|")
        print(Fore.WHITE + "|", Style.BRIGHT + Fore.GREEN + "               Created by Juno-Byte                ", Fore.WHITE + "|")
        print(Fore.WHITE + "|", Style.BRIGHT + Fore.GREEN + "                  Build v1.0.2                     ", Fore.WHITE + "|")
        print(Fore.WHITE + "|", "="*51, "|")
        print(Fore.WHITE + "|", " "*51, "|")
        print("|", Fore.MAGENTA + "                █████        █████                 ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "             █████████      █████████              ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "            ███████████    ███████████             ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "           ████████████    ████████████            ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "          █████████████    █████████████           ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "         ██████████████    █████████████           ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "         ██████████████    █████████████           ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "          █████████████    █████████████           ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "  ██████  ████████████      ████████████  ██████   ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + " █████████  █████████        █████████  █████████  ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "███████████   █████            █████   ███████████ ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "████████████         ████████         ████████████ ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "█████████████     ██████████████     █████████████ ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "█████████████    ████████████████    █████████████ ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + " ████████████  ███████████████████   ████████████  ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "  ██████████  ██████████████████████  ██████████   ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "    ███████ ██████████████████████████ ███████     ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "          ██████████████████████████████           ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "         ████████████████████████████████          ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "        ██████████████████████████████████         ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "       ████████████████████████████████████        ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "       ████████████████████████████████████        ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "        ██████████████████████████████████         ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "         ████████████████████████████████          ", Fore.WHITE + "|")
        print("|", Fore.MAGENTA + "            ████████████  ████████████             ", Fore.WHITE + "|")
        print(Fore.WHITE + "|", " "*51, "|")
        print(Fore.WHITE + "|", "Please Select An Option", " "*27, "|")
        print(Fore.WHITE + "|", Fore.GREEN + "-"*51, Fore.WHITE +  "|")
        print(Fore.WHITE + "|", "   [1] Enter New Data   ", " "*26, "|")
        print(Fore.WHITE + "|", "   [2] View Past Entries", " "*26, "|")
        print(Fore.WHITE + "|", "   [3] Open Graphing Script", " "*23, Fore.WHITE + "|")
        print(Fore.WHITE + "|", "   [4] Exit", " "*39, "|")
        print(Fore.WHITE + "|", "="*51, "|")
        choice = input("| Select an option: ")
        if choice == "1":
            insert_data()
        elif choice == "2":
            view_past_entries()
        elif choice == "3":
            open_graph_script()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
