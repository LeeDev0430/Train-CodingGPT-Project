import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/203-323.csv")

# Filter for destinations that begin in 1999
df_filtered = df[df['Begin'] == '1999']

# Count the number of destinations
number_of_destinations = df_filtered.shape[0]

# Print the number of destinations
print(number_of_destinations)