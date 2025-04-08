import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage content
url = "https://shidler.hawaii.edu/itm/people"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Identify the HTML structure
# (This step involves manually inspecting the webpage's HTML to find the tags/classes encapsulating the names)

# Step 4: Extract names
# Assuming names are within <h3> tags with a specific class, e.g., 'person-name'
# This is a hypothetical example; adjust the tag and class based on actual HTML structure

# Find all <a> tags where href starts with "/itm/directory"
people = soup.find_all("a", href=lambda href: href and href.startswith("/itm/directory"))

# Extract names
names = [a.get_text(strip=True) for a in people]
# Step 5: Print the names and count
for name in names:
    print(name)
print(f"Total number of people found: {len(names)}")
