import pandas as pd
import numpy as np

# Load data for each room from separate CSV files
rooms = {}
room_numbers = [1, 2, 3, 4, 5, 6]  # Room numbers or IDs

for room_number in room_numbers:
    filename = f'Room_{room_number}_Data.csv'  # Replace with your actual file naming convention
    data = pd.read_csv(filename)
    rooms[room_number] = data

# User preferences (change these values as needed)
user_temperature_preference = 80.5
user_noise_preference = 40

# Calculate distances for each room
room_distances = {}
for room_number, data in rooms.items():
    room_distances[room_number] = np.sqrt((data['Temperature (Fahrenheit)'] - user_temperature_preference) ** 2 +
                                          (data['Noise Level (Decibels)'] - user_noise_preference) ** 2)

# Find the room with the smallest distance (most suitable room)
best_room_number = min(room_distances, key=lambda k: room_distances[k].iloc[0])
best_room_data = rooms[best_room_number]

# Print the recommendation
print("Recommended Room:")
print("Room Number:", best_room_number)
print("Temperature (Fahrenheit):", best_room_data['Temperature (Fahrenheit)'].iloc[0])
print("Noise Level (Decibels):", best_room_data['Noise Level (Decibels)'].iloc[0])
