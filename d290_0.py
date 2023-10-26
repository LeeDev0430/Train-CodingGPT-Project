import pandas as pd

df = pd.read_csv("input files/204-435.csv")
rowing_gold = df[df["Sport"] == "Rowing"]["Gold"].tolist()[0]
print(rowing_gold)