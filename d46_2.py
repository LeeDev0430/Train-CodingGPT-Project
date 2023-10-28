
import pandas as pd

df = pd.read_csv("input files/Netflix_TV_Shows_and_Movies.csv")
df = df.dropna(subset=["imdb_score", "tmdb_score"])

genres = df["genres"].apply(eval)
exploded = df.explode("genres")

mean_scores = (
    exploded.groupby("genres")
    .agg({"imdb_score": "mean", "tmdb_score": "mean"})
    .round(2)
).reset_index()

print("Mean score by genre:")
print(mean_scores)