

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the input
df = pd.read_csv("Datasets for Bulba Multiturn SFT/watson_healthcare_modified.csv")

# Filter out any rows with less than 10 years at company
df = df[df["YearsAtCompany"] > 10]

# Map the colors based on whether the monthly income is higher or lower than the average.
# If it's above the average, the color is green. If it's below, the color is red.
colors = np.where(df["MonthlyIncome"] >= df["MonthlyIncome"].mean(), "g", "r")

# Create a scatter plot with 'YearsAtCompany' as x and 'MonthlyIncome' as y.
# Pass the colors in using the 'c' keyword argument.
plt.scatter(x=df["YearsAtCompany"], y=df["MonthlyIncome"], c=colors)

# Add a horizontal line that shows the average monthly income
# Make the line blue and dashed
plt.axhline(
    y=df["MonthlyIncome"].mean(),
    color="blue",
    linestyle="--",
    label="Average Monthly Income",
)

# Add a legend
plt.legend()

# Set the title and axis labels
plt.title("Years at Company vs. Monthly Income")
plt.xlabel("Years at Company")
plt.ylabel("Monthly Income")

# Ensure the labels aren't cut off
plt.tight_layout()

plt.show()