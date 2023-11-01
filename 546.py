


import pandas as pd

### Load dataset
data=pd.read_csv("Datasets for Bulba Multiturn SFT/Top5000.csv")

# Group data by artist, calculate average energy score
grouped_data = data.groupby("ars_name")["energy"].mean()

# Sort data based on average energy score
sorted_data = grouped_data.sort_values(ascending=False)

# Get the top 3 artists based on average energy score
top_3_artists = sorted_data.iloc[:3]

# Print the result
print("The top 3 artists with the most average energy score are:")
for index,i in top_3_artists.items():
    print(f"{index} - {i}")