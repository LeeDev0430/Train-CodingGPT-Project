

import pandas as pd

### Load dataset
data = pd.read_csv("Datasets for Bulba Multiturn SFT/Cities_with_the_Best_Work_Life_Balance_2022.csv")

# Group the data by Country and count the number of cities in each group
country_city_counts = data.groupby("Country").size()

# Find the country with the maximum number of cities
max_cities_country = country_city_counts.idxmax()

print(f"The country with the most cities is: {max_cities_country}")
