import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-477.csv")

# Find the number of laps completed by JJ Lehto
laps_completed = df[df["Driver"] == "JJ Lehto"]["Laps"].values[0]

# Print the number of laps completed
print(laps_completed)