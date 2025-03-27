import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

url = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['sales'] = df['quantity'] * df['unit_price']
    
    # Create pivot table aggregating sales by region and order_type
    pivot_table = pd.pivot_table(df, 
                                 values='sales', 
                                 index='sales_region', 
                                 columns='order_type', 
                                 aggfunc=np.sum, 
                                 margins=True,  # Adds a 'Total' column and row
                                 margins_name="Total Sales")  # Rename total column

    # Print pivot table
    print(pivot_table)

except Exception as e:
    print(f"Error reading the file: {e}")