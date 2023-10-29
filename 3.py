
import pandas as pd

# Create pandas dataframe
df = pd.DataFrame({
    'business_name': ['Starbucks', 'McDonald\\'s', 'Walmart', 'Target', 'Kroger', 'Home Depot', 'Lowe\\'s', 'Costco', 'Best Buy', 'CVS', 'Walgreens', 'Trader Joe\\'s'],
    'weekday': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'revenue': [200, 150, 300, 250, 100, 150, 200, 300, 250, 100, 150, 200],
    'holiday_flag': [False, False, False, False, False, False, True, True, True, True, True, True],
    'avg_temp': [65, 70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15],
    'gas_price': [3.50, 3.25, 3.00, 2.75, 2.50, 2.25, 2.00, 1.75, 1.50, 1.25, 1.00, 0.75],
    'cpi': [230, 225, 210, 205, 190, 185, 180, 175, 170, 165, 160, 155],
    'unemployment_rate': [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0, 2.5, 2.0]
})

# Get the day of the week with the highest unemployment rate
day_with_highest_unemployment_rate = df[df['unemployment_rate'] == df['unemployment_rate'].max()]['weekday'].iloc[0]

# Print the day of the week with the highest unemployment rate
print(day_with_highest_unemployment_rate)