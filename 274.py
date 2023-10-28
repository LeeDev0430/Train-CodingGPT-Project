import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "country_name": ["United States", "China", "India", "Brazil", "Russia"],
    "geographic_region_name": ["North America", "Asia", "Asia", "South America", "Europe"],
    "sub_region_name": ["North America", "East Asia", "South Asia", "South America", "Eastern Europe"],
    "cases_per_100k": [1000, 500, 250, 100, 50],
    "total_cases": [10000000, 5000000, 2500000, 1000000, 500000],
    "year": [2023, 2023, 2023, 2023, 2023]
})

# Sort the DataFrame by total cases in descending order
df_sorted = df.sort_values(by='total_cases', ascending=False)

# Get the top 5 countries with the highest total cases
top_5_countries = df_sorted.head(5)

# Print the top 5 countries with the highest total cases
print(top_5_countries)