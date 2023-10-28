import pandas as pd

df = pd.read_csv("input files/203-358.csv")

slowest_athlete_run_2 = df[df["Run 2"] == df["Run 2"].max()]
slowest_athlete_name = slowest_athlete_run_2["Athlete"].tolist()[0]

print(f"The slowest athlete in run 2 is {slowest_athlete_name}.")