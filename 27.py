import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Body_Region': ['Chest', 'Back', 'Shoulders', 'Triceps', 'Biceps', 'Legs', 'Legs', 'Legs'],
    'Muscle_Group': ['Chest', 'Back', 'Shoulders', 'Triceps', 'Biceps', 'Quadriceps', 'Hamstrings', 'Calves'],
    'Exercise_Name': ['Bench Press', 'Deadlift', 'Overhead Press', 'Triceps Pushdowns', 'Bicep Curls', 'Squats', 'Leg Extensions', 'Calf Raises'],
    'Workout_Time': ['30 minutes', '30 minutes', '30 minutes', '30 minutes', '30 minutes', '30 minutes', '30 minutes', '30 minutes'],
    'Repetitions': ['10-12', '10-12', '10-12', '10-12', '10-12', '10-12', '10-12', '10-12']
}

df = pd.DataFrame(data)

# Convert 'Workout_Time' to numeric for plotting
df['Workout_Time'] = df['Workout_Time'].str.replace(' minutes', '').astype(int)

# Plotting
plt.figure(figsize=(10,6))
df.boxplot(column='Workout_Time', by='Muscle_Group', grid=False)
plt.title('Box plot of workout times by muscle group')
plt.suptitle('')  # This line removes the default title that pandas puts on the plot
plt.ylabel('Workout Time (minutes)')
plt.xlabel('Muscle Group')
plt.show()
