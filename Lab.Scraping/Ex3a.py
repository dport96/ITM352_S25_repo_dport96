import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://shidler.hawaii.edu/itm/people"

# Fetch the webpage content
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Print the type of the object
print("Type of object:", type(soup))

# Print the first few lines of prettified HTML
print(soup.prettify()[:500])  # Print only the first 500 characters for brevity
