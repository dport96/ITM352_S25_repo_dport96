"""
Write Python code to define a list of taxi trip durations in miles (use values 1.1, 0.8, 2.5, 2.6). Also define a tuple of fares for the same number of trips (use values '$6.25,' '$5.25,' '$10.50,' '$8.05'). Store both the tuple and the list as values in a dictionary called trips, with keys 'miles' and 'fares.' Print out the dictionary to show what it looks like.
"""
trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)
trips = list(zip(trip_durations,trip_fares))
print(trips)

"""
trip_num = int(input('What trip do you want:')) 
print(f"Duration: {trips['miles'][trip_num - 1]} hours")
print(f"Cost: ${trips['fares'][trip_num - 1]}")
"""