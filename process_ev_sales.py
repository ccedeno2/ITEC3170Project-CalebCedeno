import pandas as pd

# Load the dataset (the uploaded file will be in the current directory)
df = pd.read_csv('GlobalEVSales2024.csv')

# Filter data for Chile and EV sales
filtered_data = df[(df['region'] == 'Chile') & (df['parameter'] == 'EV sales')]

# Display relevant columns (region, parameter, year, value)
print(filtered_data[['region', 'parameter', 'year', 'value']])
