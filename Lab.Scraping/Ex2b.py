import pandas as pd
import ssl

# Bypass SSL verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# Define the URL
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Extract tables from the webpage
tables = pd.read_html(url)

if tables:
    df = tables[0]  # Assuming the first table contains the interest rate data
    
    # Print column names to verify correct identification of "1 Mo"
    print("Columns in the DataFrame:")
    print(df.columns)

    # Identify the correct column name for "1 Mo"
    column_name = [col for col in df.columns if "1 Mo" in col][0]  # Handling potential variations in naming
    
    print("\n1-Month Interest Rates:")
    for index, row in df.iterrows():
        print(f"Date: {row[df.columns[0]]}, 1 Mo Rate: {row[column_name]}")
else:
    print("No tables found on the page.")
