
import pandas as pd

### Load dataset
data=pd.read_csv("Datasets for Bulba Multiturn SFT/Top5000.csv")
data = data.sort_values(by=['danceability'], ascending=False)
print(data[['album','danceability']].head(5))