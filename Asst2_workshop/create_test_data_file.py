import pandas as pd
import os

url = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

try:
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')
    # write first 10 rows for test data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'sales_data_test.csv')
    df.head(10).to_csv(csv_path, index=False)

except Exception as e:
    print(f"Error reading the file: {e}")