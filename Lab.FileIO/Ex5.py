import json

# Define the dictionary
data = {
    "What is the airspeed of an unladen swallow in miles/hr": [
        "12", "8", "11", "15"
    ],
    "What is the capital of Texas": [
        "Austin", "San Antonio", "Dallas", "Waco"
    ],
    "The Last Supper was painted by which artist": [
        "Da Vinci", "Rembrandt", "Picasso", "Michelangelo"
    ],
    "Which classic novel opens with the line 'Call Me Ishmael'?": [
        "Moby Dick", "Wuthering Heights", "The Old Man and the Sea", "The Scarlet Letter"
    ],
    "Frank Lloyd Wright designed a house that included a waterfall. What is the name of this house?": [
        "Fallingwater", "Watering Heights", "Mossyledge", "Taliesin"
    ]
}

# Save to a JSON file
json_filename = "quiz_questions.json"
with open(json_filename, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Dictionary saved as {json_filename}")
