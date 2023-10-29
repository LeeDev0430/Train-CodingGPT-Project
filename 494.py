import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/cars.csv")

# Filter for used cars
used_cars = df[df["Used/New"] == "Used"]

# Calculate the percentage of used cars
percentage_used = (len(used_cars) / len(df)) * 100

# Round to two decimal places
percentage_used = round(percentage_used, 2)

# Print the percentage
print(f"{percentage_used}% of the cars are used.")