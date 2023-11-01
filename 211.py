

import pandas as pd

df = pd.read_csv("Datasets for Bulba Multiturn SFT/uk_universities.csv")
filtered_universities = df[
    (df["Region"] == "Scotland") & (df["Minimum_IELTS_score"] >= 5.5)
]

print(
    f"Number of universities in Scotland with a minimum IELTS score of 5.5: {len(filtered_universities)}"
)