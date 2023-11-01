
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = pd.DataFrame({
    "Data Availability": ["Good", "Fair", "Excellent", "Poor", "Good", "Fair", "Excellent", "Poor", "Good"],
    "Affordable Housing": ["High", "Low", "High", "Low", "Medium", "High", "High", "Low", "Medium"],
    "Educational Quality": ["Excellent", "Low", "High", "Low", "Medium", "Low", "High", "Low", "Medium"],
    "Trust in Law Enforcement": ["Good", "Good", "Poor", "Excellent", "Good", "Excellent", "Poor", "Excellent", "Good"],
    "Roads and Infrastructure": ["High", "Medium", "Low", "High", "Medium", "High", "Low", "High", "Medium"],
    "Community Events": ["Many", "Fair", "Many", "Few", "Many", "Fair", "Many", "Few", "Many"],
    "Mental Wellness": ["Good", "Fair", "Excellent", "Poor", "Good", "Fair", "Excellent", "Poor", "Good"]
})

# Calculate the percentage of cities with each category
percentages = data.value_counts(normalize=True) * 100

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=percentages.index, autopct="%1.1f%%")
plt.title("Percentage of Cities with Each Category")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()