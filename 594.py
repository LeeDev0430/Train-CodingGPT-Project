

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datasets for Bulba Multiturn SFT/Gamepass_Games_v1.csv")

rating_bins = [0, 1, 2, 3, 4, 5]
rating_labels = ["0-1", "1-2", "2-3", "3-4", "4-5"]
df["RatingCategory"] = pd.cut(
    df["RATING"], bins=rating_bins, labels=rating_labels, right=False
)
rating_counts = df["RatingCategory"].value_counts(sort=False)

non_zero_counts = rating_counts[rating_counts > 0]
non_zero_labels = non_zero_counts.index.tolist()

plt.figure(figsize=(10, 7))
explode = [0.1] * len(non_zero_counts)
colors = ["yellowgreen", "lightcoral", "lightskyblue", "purple"]
plt.pie(
    non_zero_counts,
    explode=explode,
    labels=non_zero_labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Distribution of Games Based on Ratings")
plt.show()