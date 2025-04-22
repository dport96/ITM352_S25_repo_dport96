import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
trips_data_filepath = os.path.join(current_dir, 'Trips from area 8.json')
with open(trips_data_filepath, 'r') as file:
    trips_data = json.load(file)
print(trips_data())