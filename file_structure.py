 
import os

# Define the directories and file names
data_dir = 'data'
logs_dir = 'logs'
scripts_dir = 'scripts'

data_files = ['data1.csv', 'data2.csv', 'data3.csv']
logs_files = ['app.log', 'error.log']
scripts_files = ['script1.py', 'script2.py']

# Create the directories
for directory in [data_dir, logs_dir, scripts_dir]:
    os.makedirs(directory, exist_ok=True)

# Create the empty data files
for data_file in data_files:
    with open(os.path.join(data_dir, data_file), 'w') as file:
        pass

# Create the empty logs files
for log_file in logs_files:
    with open(os.path.join(logs_dir, log_file), 'w') as file:
        pass

# Create the empty scripts files
for script_file in scripts_files:
    with open(os.path.join(scripts_dir, script_file), 'w') as file:
        pass
