
# Import libraries
import pandas as pd

# Read data from CSV file
df = pd.read_csv("input files/203-781.csv")

# Get the first competition
first_competition = df["Competition"].iloc[0]

# Print the first competition
print(first_competition)