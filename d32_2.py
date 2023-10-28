import pandas as pd

# Reading the csv file
df = pd.read_csv("input files/Netflix_TV_Shows_and_Movies.csv")
 # Filter data frame based on type of Movie
df_movies = df[df["type"] == "MOVIE"]

# Filter the data frame That contain_movies released in 20th Century
df_movies_old = df_movies[df_movies["release_year"] < 2000]

# Filter the data frame that has tmdb score more than or equal to 8
df_movies_old = df_movies_old[df_movies_old["tmdb_score"] >= 8]
# Find the number of released in the 20th century
num_of_movies = len(df_movies_old)
print(f"{num_of_movies} Movies had more than or equal to 8 tmdb score that were released in the 20th century.")

