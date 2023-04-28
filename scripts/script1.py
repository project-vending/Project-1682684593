python
import pandas as pd

# Read the data files
data1 = pd.read_csv('data/data1.csv')
data2 = pd.read_csv('data/data2.csv')
data3 = pd.read_csv('data/data3.csv')

# Merge the dataframes
merged_data = pd.merge(data1, data2, on='id')
merged_data = pd.merge(merged_data, data3, on='id')

# Write the merged data to a new file
merged_data.to_csv('data/merged_data.csv', index=False)

# Log the status
with open('logs/app.log', 'a') as log_file:
    log_file.write('Merged data written to file\n')
