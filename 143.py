
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("Datasets for Bulba Multiturn SFT/Indian_Summers_Over_the_years.csv")

# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract year and month from the 'Date' column
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month


# Define a function to filter data for the given city
def filter_city_data(city_name):
    return df[
        (df["City"] == city_name)
        & (df["Year"] == 2010)
        & (df["Month"] >= 4)
        & (df["Month"] <= 5)
    ][["Date", "tempmax"]]


jaipurSummer = filter_city_data("Jaipur")
delhiSummer = filter_city_data("New Delhi")
mumbaiSummer = filter_city_data("Mumbai")

# Create a line graph for each city
plt.figure(figsize=(10, 6))
plt.plot(jaipurSummer["Date"], jaipurSummer["tempmax"], label="Jaipur")
plt.plot(delhiSummer["Date"], delhiSummer["tempmax"], color="green", label="New Delhi")
plt.plot(mumbaiSummer["Date"], mumbaiSummer["tempmax"], color="red", label="Mumbai")

# Add a shaded area above 37 degrees Celsius
plt.fill_between(
    jaipurSummer["Date"],
    37,
    jaipurSummer["tempmax"],
    color="red",
    alpha=0.3,
    label="Extreme Heat",
)
plt.fill_between(
    delhiSummer["Date"],
    37,
    delhiSummer["tempmax"],
    color="green",
    alpha=0.3,
)
plt.fill_between(
    mumbaiSummer["Date"],
    37,
    mumbaiSummer["tempmax"],
    color="red",
    alpha=0.3,
)

# Add y-axis grid
plt.grid(axis="y", alpha=0.5, linestyle="--")


# Add title, labels, legend and grid
plt.title("Max Temperature between April and May in 2010")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()

plt.tight_layout()

# Show plot
plt.show()