# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

animals = [
    "Blue whale", "Fin whale", "Sperm whale", "Sei whale", "Bowhead whale",
    "Northern Pacific right whale", "North Atlantic right whale", "Southern right whale",
    "Bryde's whale", "Humpback whale", "African bush elephant", "Asian elephant",
    "African forest elephant", "White rhinoceros", "Hippopotamus", "Giraffe",
    "Kodiak bear", "Polar bear", "Southern elephant seal", "American bison"
]

weights = [
    190, 100, 90, 45, 45, 45, 45, 45, 40, 40, 10.4, 8.15, 6.0, 4.5, 3.2, 1.2, 0.68, 0.68, 0.67, 0.64
]

# Load data in a pandas dataframe
df= pd.DataFrame()
df['animals'] = animals
df['weights'] = weights

# Last 10 animals
last_10_animals = df['animals'].tail(10)

# Print the last 10 animals
print(last_10_animals.to_string(index=False))