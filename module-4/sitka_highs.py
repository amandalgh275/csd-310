#Amanda Tirey Module 4.2 
import csv
from datetime import datetime

from matplotlib import pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
    # Get low temperatures
        low = int(row[6])
        lows.append(low)
print (f"Successfully loaded '{filename}' not found!")
print ("Make sure the CSV file is in the same directory as this script.")
sys.exit(1)

#Main menu loop
while True:
    print("\n" + "="*50)
    print("SITKA WEATHER DATA VISUALIZER")
    print("="*50)
    print("H - View High Temperatures (red line)")
    print("L - View Low Temperatures (blue line)")
    print("E - Exit the program")
    print("="*50)

    choice = input("Enter your choice (H/L/E): ").strip().upper()
    if choice == 'H':
        # Plot the high temperatures.
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red',linewidth=2)

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=20)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=14)

        plt.tight_layout()
        plt.show()
        
    elif choice == 'L':
        # Plot the low temperatures (BLUE)
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue',linewidth=2)

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=20)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=14)

        plt.tight_layout()
        plt.show()

    elif choice == 'E':
    # Exit the program
        print("\n" + "="*50)
        print("Exiting the program. Goodbye!")
        print("="*50)
        sys.exit(0)
    else:
        print("Invalid choice. Please enter H, L, or E.")

plt.show()