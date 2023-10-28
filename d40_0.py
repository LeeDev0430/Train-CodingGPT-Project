import pandas as pd

data = pd.read_csv("input files/nasa_neo_v2.csv")

hazardous = data[data["hazardous"] == True]

avg_velocity = hazardous["relative_velocity"].mean()
avg_magnitude = hazardous["absolute_magnitude"].mean()
avg_miss_distance = hazardous["miss_distance"].mean()

print(
    f"The average velocity is {avg_velocity:.2f} km/s, the average magnitude is {avg_magnitude:.2f}, and the average miss distance is {avg_miss_distance:.2f} km."
)