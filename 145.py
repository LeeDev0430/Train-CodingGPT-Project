import pandas as pd

# Read CSV
df = pd.read_csv("Datasets for Bulba Multiturn SFT/Indian_Summers_Over_the_years.csv")

# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Find the highest maximum temperature
max_temp = df["tempmax"].max()

# Determine on what day it was
max_temp_day = df[df["tempmax"] == max_temp]["Date"].values[0]

# Determine which city
max_temp_city = df[df["tempmax"] == max_temp]["City"].values[0]

# Convert temp to fahrenheit
max_temp_fahrenheit = (max_temp * 9) / 5 + 32

print(
    "The highest maximum temperature was {}°C on {} in {}. This is equal to {}°F.".format(
        max_temp, max_temp_day, max_temp_city, max_temp_fahrenheit
    )
)
