import pandas as pd

df = pd.read_csv("input files/204-735.csv")

italy_count = len(df[df["Qualification"] == "q"])
other_teams_count = len(df[(df["Qualification"] == "q") & (df["Team"] != "Italy")])

print(other_teams_count)