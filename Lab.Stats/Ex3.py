import json
import os
import matplotlib.pyplot as plt
import math
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
trips_data_filepath = os.path.join(current_dir, 'Trips from area 8.json')
df = pd.read_json(trips_data_filepath)
df = df.dropna()

grouped = df.groupby('payment_type')['tips'].sum()
grouped.plot(kind='bar', color='skyblue')
plt.title('Total Tips by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Total Tips')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()