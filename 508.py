
import pandas as pd

df = pd.read_csv("input files/blizzard_games.csv")

print(df["Name"].tolist())
