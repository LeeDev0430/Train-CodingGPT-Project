import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary from data table
data = {'Team': ['Boston Celtics', 'Los Angeles Lakers', 'Golden State Warriors', 'Milwaukee Bucks', 'San Antonio Spurs', 'Chicago Bulls', 'Houston Rockets', 'Miami Heat', 'Detroit Pistons', 'Philadelphia 76ers'],
        'Championships': [17, 17, 7, 2, 2, 6, 2, 3, 3, 3],
        'Games Won': [3601, 3483, 2592, 1775, 2186, 1568, 2459, 934, 2127, 2785],
        'Games Lost': [2182, 2162, 1995, 1718, 1908, 982, 2238, 757, 1966, 2606],
        'Stadium Capacity': ['TD Garden (19,156)', 'Crypto.com Arena (19,068)', 'Chase Center (18,064)', 'Fiserv Forum (17,341)', 'AT&T Center (18,418)', 'United Center (22,442)', 'Toyota Center (18,055)', 'FTX Arena (19,600)', 'Little Caesars Arena (20,332)', 'Wells Fargo Center (20,478)']}

# Create DataFrame object from the dictionary structure
df = pd.DataFrame(data)

# Create figure size
plt.figure(figsize=(10,6))

# Create Bar plot by championships
plt.bar(df['Team'], df['Championships'], color=['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'brown', 'black'])

# Set labels in rotation 90
plt.xticks(rotation=45)

# Set title and axis labels
plt.title('Championships by Team')
plt.xlabel('Team')
plt.ylabel('Championships')

# Add horizontal grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show graph
plt.show()