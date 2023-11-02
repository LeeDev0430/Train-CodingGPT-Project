import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/203-512.csv")

# Convert the "Release Date" column to datetime
df["Release Date"] = pd.to_datetime(df["Release Date"], errors="coerce")

# Filter for albums/singles released after the year 2000
df_filtered = df[df["Release Date"].dt.year > 2000]

# Count the number of albums/singles
number_of_albums_singles = df_filtered.shape[0]

# Print the results
print(number_of_albums_singles)