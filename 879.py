
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-596.csv")

# Get the last year that Chasetown won
last_year_won = df[df['Winners'].str.contains("Chasetown")]['Year'].max()

# Print the last year that Chasetown won
print(last_year_won)