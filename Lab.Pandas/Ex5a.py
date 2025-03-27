import pandas as pd

file_id = "1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
url = f"https://drive.google.com/uc?id={file_id}"

import pandas as pd
df = pd.read_csv(url)

print(df.head())

print(f'The dims are {df.shape}')