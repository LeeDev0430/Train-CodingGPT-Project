
import pandas as pd

# Create a pandas dataframe
df = pd.DataFrame({
    'Animal': ['Sea anemone', 'Garden snail', 'Pink starfish', 'Dwarf seahorse', 'Three-toed sloth', 'Giant tortoise', 'Banana slug', 'Slow loris', 'Gila monster', 'Koala'],
    'Speed':  [0.0055, 0.00417, 0.0417, 0.00694, 1, 4, 0.3, 10, 15, 15]
})

# Calculate the average speed
average_speed = df['Speed'].mean()

# Calculate the variance of speed
variance_of_speed = df['Speed'].var()

# Print the results
print('Average speed:', average_speed)
print('Variance of speed:', variance_of_speed)
