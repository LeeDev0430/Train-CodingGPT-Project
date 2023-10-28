
import pandas as pd

df = pd.read_csv("input files/201-46.csv")
df = df[df["Position"] == "right"]
df = df[df["Drainage basin area [km2]"] == 11.8]
print(df["Name"])