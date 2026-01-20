# Amanda Tirey Module 4.2
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

# Read data
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))
        lows.append(int(row[6]))

print(f"Loaded {len(dates)} days of weather data")

# Menu loop
while True:
    print("\n" + "="*40)
    print("WEATHER DATA MENU")
    print("="*40)
    print("H - High temperatures (red)")
    print("L - Low temperatures (blue)")
    print("E - Exit")
    print("="*40)
    
    choice = input("Enter H, L, or E: ").upper().strip()
    
    if choice == 'H':
        plt.figure(figsize=(10, 6))
        plt.plot(dates, highs, 'r-', linewidth=2)
        plt.title("Daily High Temperatures - 2018")
        plt.ylabel("Temperature (F)")
        plt.tight_layout()
        plt.show()
        
    elif choice == 'L':
        plt.figure(figsize=(10, 6))
        plt.plot(dates, lows, 'b-', linewidth=2)
        plt.title("Daily Low Temperatures - 2018")
        plt.ylabel("Temperature (F)")
        plt.tight_layout()
        plt.show()
        
    elif choice == 'E':
        print("\nThank you! Goodbye!")
        sys.exit(0)
        
    else:
        print("Invalid choice. Please try again.")