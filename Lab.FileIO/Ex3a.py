import requests
import csv
import io

# File URL for direct download
file_url = "https://drive.google.com/uc?id=10X2Icx78XKTbt3ZRj3F-FlzmW_NugEpz"

# Fetch the CSV file
response = requests.get(file_url)
response.raise_for_status()  # Ensure the request was successful

# Read CSV data
csv_data = io.StringIO(response.text)
reader = csv.reader(csv_data)

# Read the header row
headers = next(reader)

# Find the index of relevant fields
fare_index = headers.index("Fare")
trip_miles_index = headers.index("Trip Miles")

# Initialize variables for calculations
total_fare = 0
max_trip_distance = 0
fare_count = 0

# Process the first 1,000 lines of data
for i, row in enumerate(reader):
    if i >= 1000:
        break  # Stop after 1,000 rows
    
    try:
        fare = float(row[fare_index])
        trip_miles = float(row[trip_miles_index])

        total_fare += fare
        max_trip_distance = max(max_trip_distance, trip_miles)
        fare_count += 1
    except ValueError:
        # Handle missing or invalid values
        continue

# Calculate average fare
average_fare = total_fare / fare_count if fare_count else 0

# Print results
print(f"Total Fare: ${total_fare:,.2f}")
print(f"Average Fare: ${average_fare:,.2f}")
print(f"Maximum Trip Distance: {max_trip_distance:.2f} miles")
