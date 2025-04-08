import urllib.request
import ssl

# Bypass SSL verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# Define the URL to open
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

with urllib.request.urlopen(url) as response:
    # Iterate through each line in the response
    for line in response:
        # Decode the line
        decoded_line = line.decode('utf-8')
        # Print only if it contains a <title> tag
        if "<title>" in decoded_line:
            print(decoded_line.strip())