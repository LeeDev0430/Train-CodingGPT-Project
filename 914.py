
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/203-798.csv")

# Filter for rows where the party is not Liberal and Country League
df_filtered = df[df['Party'] != "Liberal and Country League"]

# Sort by number of votes in descending order
df_filtered = df_filtered.sort_values(by=['Votes'], ascending=False)

# Get the party with the third highest number of votes
third_highest_party = df_filtered.iloc[2]['Party']

# Print the party with the third highest number of votes
print(third_highest_party)