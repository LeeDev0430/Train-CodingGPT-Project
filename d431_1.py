
import pandas as pd

df = pd.read_csv("input files/204-145.csv")
df["Date of death"] = pd.to_datetime(df["Date of death"], format="%B %d, %Y")
deaths_by_party = df.groupby("Party")["Date of death"].count()
party_with_most_deaths = deaths_by_party.idxmax()

print(f"Party with the most deaths: {party_with_most_deaths}")