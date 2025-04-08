import pandas as pd
import ssl

# Bypass SSL verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# Define the URL
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Extract tables from the webpage
tables = pd.read_html(url)

# Print the number of tables found
print(f"Number of tables found: {len(tables)}")

# Print the first few columns of the first table
if tables:
    df = tables[0]  # Assuming the first table contains the interest rate data
    print("Columns in the DataFrame:")
    print(df.columns)
    print(df.head())  # Display the first few rows
else:
    print("No tables found on the page.")
