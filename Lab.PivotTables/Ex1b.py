import pandas as pd

pd.set_option('display.max_columns', None)

url = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    print(df.head())

except Exception as e:
    print(f"Error reading the file: {e}")