import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datasets for Bulba Multiturn SFT/Cities_with_the_Best_Work_Life_Balance_2022.csv")

# Filter for cities in Germany
df = df[df["Country"] == "Germany"]

# Change "Frankfurt (am Main)" to "Frankfurt"
df["City"] = df["City"].apply(lambda x: x.replace(" (am Main)", ""))

# Sort by city name
df = df.sort_values(by="City")

# Extract the columns to plot
affordability = df["Affordability"]
safety = df["City Safety"]
wellness = df["Wellness and Fitness"]

# Set the y-axis range
plt.ylim(60, 90)

# Create the line chart
plt.plot(affordability, label="Affordability")
plt.plot(safety, label="Safety")
plt.plot(wellness, label="Wellness")

# Add labels and title
plt.xlabel("City")
plt.ylabel("Score")
plt.title("Affordability, Safety, and Wellness of German Cities")

# Add legend
plt.legend()

# Show the plot
plt.show()