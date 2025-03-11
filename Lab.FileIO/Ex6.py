import json

# JSON file name
json_filename = "quiz_questions.json"

# Read and print the JSON file
with open(json_filename, "r") as json_file:
    data = json.load(json_file)

# Print the dictionary in a readable format
print(json.dumps(data, indent=4))
