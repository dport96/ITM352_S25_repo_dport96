import pandas as pd
import requests
import io
import matplotlib.pyplot as plt

# Direct download link
url = "https://drive.google.com/uc?id=1-kjcJHN_pCJfB-f3_2xgQNF5U-5PitjU"

# Fetch the file
response = requests.get(url)
response.raise_for_status()  # Raise an error if download failed

# Load JSON into DataFrame
df = pd.read_json(io.StringIO(response.text))

# Create scatter plot
plt.scatter(df['fare'], df['tips'], color='blue', marker='o')

# Show the plot
plt.grid(True)
plt.show()
