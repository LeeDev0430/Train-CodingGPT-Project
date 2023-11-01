
import pandas as pd

# read the input data
df = pd.read_csv("Datasets for Bulba Multiturn SFT/watson_healthcare_modified.csv")

# count the number of employees under 18 years of age
print(
    len(df[df.Age < 18]),
    "employees are under 18 years of age.",
)