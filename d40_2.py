
import pandas as pd

data = pd.read_csv("input files/nasa_neo_v2.csv")

fastest = data.iloc[data["relative_velocity"].idxmax()]

print(f"The id of the fastest object is {fastest.iloc[0]}")

