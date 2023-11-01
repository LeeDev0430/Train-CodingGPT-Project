

import pandas as pd

# Read CSV
df = pd.read_csv("Datasets for Bulba Multiturn SFT/watson_healthcare_modified.csv")

# Drop duplicates
df_unique = df.drop_duplicates()

# Group by Department
dept_grouped = df_unique.groupby("Department")

# Mean Job Satisfaction
mean_job_satisfaction_by_dept = dept_grouped["JobSatisfaction"].mean()

# Max average job satisfaction
highest_avg_job_satisfaction_dept = mean_job_satisfaction_by_dept.idxmax()
highest_avg_job_satisfaction = mean_job_satisfaction_by_dept.max()

# Average Job Satisfaction
avg_job_satisfaction = mean_job_satisfaction_by_dept.mean()

# Difference from average
difference_from_average = highest_avg_job_satisfaction - avg_job_satisfaction

print(
    f"The department with the highest job satisfaction is {highest_avg_job_satisfaction_dept} with an average job satisfaction of {highest_avg_job_satisfaction:.2f}, which is {difference_from_average:.2f} above the average job satisfaction."
)