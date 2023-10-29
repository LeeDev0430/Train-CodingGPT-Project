import pandas as pd

df = pd.read_csv("input files/BoeingOrdersandDeliveries.csv")

num_unique_countries = df["Country"].nunique()

print(f"There are {num_unique_countries} unique countries who ordered from Boeing.")
