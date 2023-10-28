import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
df = pd.DataFrame({
    "body_area": ["Chest", "Back", "Triceps", "Biceps", "Shoulders", "Abs", "Legs", "Legs", "Calves", "Glutes"],
    "target_muscle": ["Pectoralis Major", "Latissimus Dorsi", "Triceps Brachii", "Biceps Brachii", "Deltoids", "Rectus Abdominis", "Quadriceps", "Hamstrings", "Gastrocnemius", "Gluteus Maximus"],
    "exercise": ["Bench Press", "Pull-Ups", "Triceps Pushdowns", "Bicep Curls", "Overhead Press", "Crunches", "Squats", "Deadlifts", "Calf Raises", "Hip Thrusts"],
    "workout_length": [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
    "reps": [10, 10, 10, 10, 10, 20, 10, 10, 20, 10]
})

# Create a time series of workout lengths over time
workout_lengths_over_time = df.groupby("workout_length")["workout_length"].count()

# Plot the time series
plt.plot(workout_lengths_over_time.index, workout_lengths_over_time.values)
plt.xlabel("Workout Length (minutes)")
plt.ylabel("Number of Workouts")
plt.title("Time Series of Workout Lengths")
plt.show()