
import pandas as pd

# Create a DataFrame from the provided data
df = pd.DataFrame({
    "country_name": ["United States", "China", "India", "Brazil", "Russia"],
    "geographic_region_name": ["North America", "Asia", "Asia", "South America", "Europe"],
    "sub_region_name": ["North America", "East Asia", "South Asia", "South America", "Eastern Europe"],
    "cases_per_100k": [1000, 500, 250, 100, 50],
    "total_cases": [10000000, 5000000, 2500000, 1000000, 500000],
    "year": [2023, 2023, 2023, 2023, 2023]
})

# Filter the DataFrame to only include data for the year 2023
df_filtered = df[df['year'] == 2023]

# Find the country with the highest number of cases
country_with_highest_cases = df_filtered[df_filtered['total_cases'] == df_filtered['total_cases'].max()]['country_name'].values[0]

# Print the country with the highest number of cases
print(country_with_highest_cases)