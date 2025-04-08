import urllib.request
import ssl

# Bypass SSL verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# Define the URL to open
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

# Open the URL
with urllib.request.urlopen(url) as response:
    print(response)
    # Read the response
   # html = response.read()
    # Print the raw HTML response
  #  print(html.decode('utf-8'))
