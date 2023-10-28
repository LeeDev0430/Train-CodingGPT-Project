import pandas as pd

df = pd.read_csv("input files/mobile-phone-brands-by-country.csv")
df_grouped = df.groupby("Region").size().to_frame(name="count").reset_index()
print(df_grouped)