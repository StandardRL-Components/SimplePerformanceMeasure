import time
import csv
import psutil
from datetime import datetime

# Initialize a list to store the data
data = []

# Record the start time
start_time = time.time()

print("Monitoring CPU utilization, RAM usage, and CPU temperature... Press Ctrl+C to stop.")

try:
    while True:
        # Calculate elapsed time in milliseconds
        elapsed_time = (time.time() - start_time) * 1000

        # Get CPU utilization
        cpu_util = psutil.cpu_percent(interval=0)

        # Get RAM usage
        ram_usage = psutil.virtual_memory().percent

        # Get CPU temperature (specific to Raspberry Pi)
        try:
            temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
        except KeyError:
            temp = None  # Temperature sensor not available

        # Append the data
        data.append([elapsed_time, cpu_util, ram_usage, temp])

        # Wait for 0.5 seconds
        time.sleep(0.5)

except KeyboardInterrupt:
    # Handle keyboard interrupt and write data to CSV
    print("\nSaving data to results.csv...")

    # Specify the CSV file headers
    headers = ["Time (ms)", "CPU Utilization (%)", "RAM Usage (%)", "CPU Temperature (C)"]

    # Write to results.csv
    with open("results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print("Data saved to results.csv successfully.")