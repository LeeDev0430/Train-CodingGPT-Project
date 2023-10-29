import pandas as pd

# Create a pandas dataframe
df = pd.DataFrame({
    "country": ["United States", "India", "China", "Brazil", "Russia", "Japan", "Germany", "United Kingdom", "France", "Italy", "Canada", "Australia", "New Zealand"],
    "georegion": ["North America", "Asia", "Asia", "South America", "Europe", "Asia", "Europe", "Europe", "Europe", "Europe", "North America", "Australia and New Zealand", "Australia and New Zealand"],
    "subregion": ["North America", "South Asia", "East Asia", "South America", "Eastern Europe", "East Asia", "Western Europe", "Western Europe", "Western Europe", "Southern Europe", "North America", "Australia", "New Zealand"],
    "cases_per_hundred_thousand": [1000, 500, 250, 100, 50, 25, 10, 5, 250, 250, 250, 250, 250],
    "total_cases": [1000000, 500000, 250000, 100000, 50000, 25000, 10000, 5000, 2000, 1000, 500, 250, 125],
    "year": [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023]
})

# Filter for countries in Asia
df_filtered = df[df['georegion'] == 'Asia']

# Sort by cases per hundred thousand in descending order
df_filtered = df_filtered.sort_values(by=['cases_per_hundred_thousand'], ascending=False)

# Get the country with the highest number of cases per hundred thousand people
country_with_highest_cases = df_filtered['country'].iloc[0]

# Print the country with the highest number of cases per hundred thousand people
print(country_with_highest_cases)