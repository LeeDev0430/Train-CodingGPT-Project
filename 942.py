
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-300.csv")

# Convert the "Date from" and "Date to" columns to datetime format
df["Date from"] = pd.to_datetime(df["Date from"], errors="coerce")
df["Date to"] = pd.to_datetime(df["Date to"], errors="coerce")

# Filter for players whose "to" date is in March and "from" date is in January
filtered_df = df[(df["Date to"].dt.month == 3) & (df["Date from"].dt.month == 1)]

# Get the player's name
player_name = filtered_df["Name"].iloc[0]

# Print the player's name
print(player_name)