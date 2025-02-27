# Define tuples
celebrities_tuple = ("Taylor Swift", "Lionel Messi", "Max Verstappen", "Keanu Reeves", "Angelina Jolie")
ages_tuple = (34, 36, 26, 59, 48)  # Adjusted ages

# Initialize lists
celebrities_list = []
ages_list = []

# Iterate through tuples and append values to lists
for celeb in celebrities_tuple:
    celebrities_list.append(celeb)

for age in ages_tuple:
    ages_list.append(age)

# Store lists in a dictionary
celebrities_dict = {
    "celebrities": celebrities_list,
    "ages": ages_list
}

# Print the result
print(celebrities_dict)
