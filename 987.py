
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("input files/204-828.csv")

# Get the maximum value of the "Threads per inch" column
max_threads_per_inch = df["Threads per inch"].max()

# Print the maximum value of the "Threads per inch" column
print(max_threads_per_inch)