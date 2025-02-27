# Given tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Initialize counter
string_count = 0

# Loop through each element in the tuple
for item in data:
    if type(item) == str:  # Check if the element is a string
        string_count += 1

# Print the result
print(f"There are {string_count} strings in the tuple.")
