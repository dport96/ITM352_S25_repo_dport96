import pandas as pd

# Load JSON file from Google Drive
url = "https://drive.google.com/uc?id=1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus"
df = pd.read_json(url)

# Print summary statistics
print(df.describe())

print(df)
# Print the median for numerical columns
print("\nMedian values:")
print(df['fare'].median())
