import pandas as pd

df = pd.read_csv("Datasets for Bulba Multiturn SFT/Cities_with_the_Best_Work_Life_Balance_2022.csv")
max_vacations = df["Minimum Vacations Offered (Days)"].max()

cities_with_highest_vacations = df[
    df["Minimum Vacations Offered (Days)"] == max_vacations
]["City"]

city = cities_with_highest_vacations.iloc[0]

covid_impact = df[df["City"] == city]["Covid Impact"].values[0]
covid_support = df[df["City"] == city]["Covid Support"].values[0]

impact_to_support_ratio = (covid_impact / covid_support) * 100

print(
    f"The city of {city} has a COVID impact to support ratio of {impact_to_support_ratio:.2f}%."
)