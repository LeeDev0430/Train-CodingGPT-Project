import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-893.csv")

# Convert the Time column to datetime
df["Time"] = pd.to_datetime(df["Time"], format='%M:%S.%f')

# Filter for athletes with times under 8 minutes
filtered_df = df[df["Time"] < pd.to_datetime('8:00.00')]

# Count the number of athletes in the filtered DataFrame
number_of_athletes = filtered_df.shape[0]

# Print the number of athletes with times under 8 minutes
print(number_of_athletes)