import csv
import random
from datetime import datetime, timedelta

# Number of rooms and rows of data per room
num_rooms = 6
num_rows_per_room = 100

# Generate data for each room
for room_num in range(1, num_rooms + 1):
    # Create a CSV file for the room
    file_name = f"Room_{room_num}_Data.csv"
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['room_ID','Timestamp', 'Temperature (Fahrenheit)', 'Noise Level (Decibels)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the CSV header
        writer.writeheader()
        
        # Generate and write mock data for the room
        timestamp = datetime(2023, 9, 1, 8, 0, 0)
        for _ in range(num_rows_per_room):
        
            temperature = round(random.uniform(70, 75), 1)
            noise_level = random.randint(35, 60)
            writer.writerow({'room_ID': room_num,
                             'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                             'Temperature (Fahrenheit)': temperature,
                             'Noise Level (Decibels)': noise_level})
            timestamp += timedelta(minutes=15)

print("CSV files generated successfully.")
