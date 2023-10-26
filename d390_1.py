import pandas as pd

df = pd.read_csv('input files/203-783.csv')

division_counts = df.groupby('Division')['Place'].count()
max_count = division_counts.max()
max_division = division_counts.idxmax()

print(f'Division with the most ranks: {max_division}')