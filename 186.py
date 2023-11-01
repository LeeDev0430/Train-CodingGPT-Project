import pandas as pd

df = pd.read_csv("Datasets for Bulba Multiturn SFT/uk_universities.csv")
filtered_universities = df[
    (df["Founded_year"] >= 1800) & (df["Founded_year"] <= 1900)
]

percentage_of_universities_founded_between_1800_and_1900 = (
    len(filtered_universities) / len(df)
) * 100

print(
    f"Percentage of universities that were founded between 1800 and 1900, including both of these years: {percentage_of_universities_founded_between_1800_and_1900:.2f}%"
)