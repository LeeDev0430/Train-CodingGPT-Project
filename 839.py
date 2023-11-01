
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-174.csv")

# Count the number of unique nationalities after rank 5
number_of_nationalities = df[df['Rank'] > 5]['Nationality'].nunique()

# Print the number of nationalities
print(number_of_nationalities)