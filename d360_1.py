
import pandas as pd

df = pd.read_csv("input files/203-60.csv")
last_row = df.iloc[-1]
opponent = last_row["Opponent in the final"]

print(opponent)