import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/203-245.csv")

# Filter for races after 1995
df_filtered = df[df['Year'] > 1995]

# Get the highest position
highest_position = df_filtered['Position'].min()

# Print the highest position
print(highest_position)