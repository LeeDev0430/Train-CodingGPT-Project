
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the CSV into a Pandas DataFrame
df = pd.read_csv("Datasets for Bulba Multiturn SFT/watson_healthcare_modified.csv")

# Filter for employees worked 1 and over
df_filtered = df[df['NumCompaniesWorked'] >= 1]

# Calculate average monthly income every number of companies worked
df_average_monthly_income = df_filtered.groupby(['NumCompaniesWorked'])['MonthlyIncome'].mean()
num_companies_worked = df_average_monthly_income.index.to_numpy()
average_monthly_income = df_average_monthly_income.to_numpy()

# Sort together by number of companies worked
df_temp = pd.DataFrame({'NumCompaniesWorked': num_companies_worked, 'AverageMonthlyIncome': average_monthly_income})
df_temp = df_temp.sort_values(by=['NumCompaniesWorked'],ascending=True)

num_companies_worked = df_temp['NumCompaniesWorked'].to_numpy()
average_monthly_income = df_temp['AverageMonthlyIncome'].to_numpy()

# Plot average monthly income vs number of companies worked
plt.plot(num_companies_worked, average_monthly_income)

# Set the title and axis labels
plt.title("Average Monthly Income by Number of Companies Worked")
plt.xlabel("Number of Companies Worked")
plt.ylabel("Average Monthly Income")

# Show the plot
plt.show()