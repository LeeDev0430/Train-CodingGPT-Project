import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/203-510.csv")

# Sort by population in descending order
df = df.sort_values(by=['Population'], ascending=False)

# Get the township with the largest population
township_with_largest_population = df['Township'].iloc[0]

# Print the township with the largest population
print(township_with_largest_population)