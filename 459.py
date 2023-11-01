import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
df = pd.DataFrame({
    "body_part": ["Chest", "Back", "Legs", "Shoulders", "Biceps", "Triceps"],
    "muscle_type": ["Pectoralis Major", "Latissimus Dorsi", "Quadriceps", "Deltoids", "Biceps Brachii", "Triceps Brachii"],
    "exercise": ["Bench Press", "Pull-Ups", "Squats", "Overhead Press", "Bicep Curls", "Triceps Pushdowns"],
    "number_of_sets": [3, 3, 3, 3, 3, 3],
    "reps_per_set": [10, 10, 10, 10, 10, 10]
})

# Create a histogram of the number of sets per exercise
plt.hist(df["number_of_sets"])
plt.xlabel("Number of Sets")
plt.ylabel("Frequency")
plt.title("Distribution of Number of Sets per Exercise")
plt.show()