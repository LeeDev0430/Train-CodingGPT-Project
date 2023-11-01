
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = pd.DataFrame({
    "Entity Name": ["United States", "Canada", "Mexico", "Brazil", "Argentina", "Colombia", "Chile"],
    "Country Code": ["US", "CA", "MX", "BR", "AR", "CO", "CL"],
    "Year": [2023, 2023, 2023, 2023, 2023, 2023, 2023],
    "Cellular Subscriptions": [250, 200, 150, 100, 75, 50, 25],
    "Internet Users Percentage": [90, 80, 70, 50, 40, 30, 20],
    "Number of Internet Users": [225, 160, 105, 50, 30, 15, 10],
    "Broadband Subscriptions": [150, 100, 75, 50, 35, 25, 15]
})

# Extract the broadband subscriptions
broadband_subscriptions = data["Broadband Subscriptions"]

# Try converting broadband subscriptions into numerics before plotting the distribution
try:
  # If it is string type, remove all characters except numbers, ".", "+" or "-".
  if pd.api.types.is_string_dtype(broadband_subscriptions):
    for i in range(len(broadband_subscriptions)):
      broadband_subscriptions.iloc[i] = re.sub(r"[^\\d\\-+\\.]", "", broadband_subscriptions.iloc[i])
  broadband_subscriptions = pd.to_numeric(broadband_subscriptions)
except:
  pass

# Plot the distribution of the broadband subscriptions
plt.hist(broadband_subscriptions)
plt.xlabel("Broadband Subscriptions")
plt.ylabel("Number of Entities")
plt.title("Distribution of Broadband Subscriptions in 2023")
plt.show()