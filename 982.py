
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-423.csv")

# Convert the "Listing date" column to datetime format
df["Listing date"] = pd.to_datetime(df["Listing date"], errors="coerce")

# Filter for listings with a listing date of April 14, 1961
df_filtered = df[df["Listing date"] == "April 14, 1961"]

# Get the name of the listing
name = df_filtered["Name"].iloc[0]

# Print the name
print(name)