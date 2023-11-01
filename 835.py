
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-275.csv")

# Get the first asian country
first_asian_country = df[df['Opponent'].str.contains("Japan")]["Opponent"].values[0]

# Print the first asian country
print(first_asian_country)