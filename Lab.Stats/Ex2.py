import json
import os
import matplotlib.pyplot as plt
import math

current_dir = os.path.dirname(os.path.abspath(__file__))
trips_data_filepath = os.path.join(current_dir, 'Trips from area 8.json')
with open(trips_data_filepath, 'r') as file:
    trips_data = json.load(file)
miles = [float(d['trip_miles']) for d in trips_data]

bins_guess = int(math.sqrt(len(miles)))
plt.hist(miles, bins=bins_guess, edgecolor='black')
plt.show()