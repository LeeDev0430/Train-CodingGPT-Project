
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-127.csv")

# Filter for winner matches
df_filtered = df[df['Outcome'] == "Winner"]

# Sort by date
df_filtered = df_filtered.sort_values(by=['Date'], ascending=False)

# Get the tournament name of the last match
last_tournament_name = df_filtered['Tournament'].iloc[0]

# Print the last tournament name
print(last_tournament_name)