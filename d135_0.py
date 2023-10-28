import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("input files/Tree_Species.csv")

plt.figure(figsize=(10, 6))
plt.scatter(df["Height"], df["Trunks"])
plt.title("Number of Trunks vs. Height")
plt.xlabel("Height")
plt.ylabel("Number of Trunks")
plt.grid(True)
plt.show()