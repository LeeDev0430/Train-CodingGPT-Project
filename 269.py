import pandas as pd

# Load data
df = pd.read_csv("Datasets for Bulba Multiturn SFT/uk_universities.csv")

# Convert to numeric
df["Student_satisfaction"] = (
    df["Student_satisfaction"].str.rstrip("%").astype("float")
)

# Group by type
grouped_by_type = df.groupby("Control_type")["Student_satisfaction"].mean()

# Highest satisfaction
highest_satisfaction_type = grouped_by_type.idxmax()
highest_satisfaction_value = grouped_by_type.max()

# Print result
print(
    f"On average, the type of university with the highest student satisfaction is '{highest_satisfaction_type}' with a student satisfaction of {highest_satisfaction_value:.2f}%. "
)