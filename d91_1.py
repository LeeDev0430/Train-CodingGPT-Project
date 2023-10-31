import pandas as pd

df = pd.read_csv("input files/Netflix_TV_Shows_and_Movies.csv")
max_seasons = df["seasons"].max()

show_with_max_seasons = df[
    (df["type"] == "SHOW") & (df["seasons"] == max_seasons)
]["title"].values[0]

print(
    f"The show that ran for {int(max_seasons)} seasons is:",
    show_with_max_seasons,
)