import pandas as pd

# Create a dataframe
df = pd.DataFrame({
'manufacturer': ['Toyota', 'Honda', 'Nissan', 'Chevrolet', 'Ford', 'Dodge', 'Chrysler', 'Volkswagen', 'Hyundai', 'Kia'],
'model': ['Camry', 'Accord', 'Altima', 'Malibu', 'Fusion', 'Charger', 'Chrysler', 'Jetta', 'Elantra', 'Optima'],
'fuel_efficiency': [28, 30, 29, 27, 28, 25, 26, 29, 31, 30],
'engine_size': [2.5, 2.4, 2.5, 1.5, 2.0, 3.6, 3.6, 1.4, 2.0, 2.4],
'horsepower': [179, 185, 188, 163, 175, 300, 292, 150, 170, 180],
'weight': [3, 3, 3, 3, 3, 4, 4, 3, 3, 3],
'acceleration': [8.5, 7.5, 8.0, 9.0, 8.5, 6.5, 7.0, 9.5, 8.0, 7.5],
'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029],
'origin': ['Japan', 'Japan', 'Japan', 'United States', 'United States', 'United States', 'United States', 'Germany', 'South Korea', 'South Korea']
})

# Print the standard deviation of sepal width
print(df['engine_size'].std())