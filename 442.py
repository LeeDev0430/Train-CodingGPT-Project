
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = pd.DataFrame({
    "body_area": ["Chest", "Back", "Triceps", "Biceps", "Shoulders", "Abs", "Legs", "Legs", "Calves", "Glutes"],
    "target_muscle": ["Pectoralis Major", "Latissimus Dorsi", "Triceps Brachii", "Biceps Brachii", "Deltoids", "Rectus Abdominis", "Quadriceps", "Hamstrings", "Gastrocnemius", "Gluteus Maximus"],
    "exercise": ["Bench Press", "Pull-Ups", "Triceps Pushdowns", "Bicep Curls", "Overhead Press", "Crunches", "Squats", "Deadlifts", "Calf Raises", "Hip Thrusts"],
    "workout_length": [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
    "reps": [10, 10, 10, 10, 10, 20, 10, 10, 20, 10]
})

# Create a pivot table to get the average workout length for each body area and target muscle
pivot_table = data.pivot_table(index="body_area", columns="target_muscle", values="workout_length", aggfunc="mean")

# Create a heatmap from the pivot table
plt.figure(figsize=(10, 6))
heatmap = plt.pcolor(pivot_table, cmap="YlGnBu")

# Add labels and title to the heatmap
plt.xlabel("Target Muscle")
plt.ylabel("Body Area")
plt.title("Heatmap of Workout Lengths by Body Area and Target Muscle")

# Add a colorbar to the heatmap
plt.colorbar(heatmap)

# Show the heatmap
plt.show()