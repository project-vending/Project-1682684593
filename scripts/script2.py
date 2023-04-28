python
import pandas as pd

data = pd.read_csv('data/data1.csv')
filtered_data = data[data['column'] == 'value']
filtered_data.to_csv('data/filtered_data.csv', index=False)
