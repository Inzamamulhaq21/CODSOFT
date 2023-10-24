import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the MovieLens dataset
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Merge movie details with user ratings
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Create a user-item matrix
user_movie_matrix = pd.pivot_table(movie_ratings, index='userId', columns='title', values='rating')

# Calculate user-user similarity using cosine similarity
user_similarity = cosine_similarity(user_movie_matrix.fillna(0))

# Define a function to get movie recommendations for a user
def get_movie_recommendations(user_id, top_n=10):
    user_row = user_movie_matrix.loc[user_id].fillna(0)
    user_scores = user_similarity.dot(user_row)
    recommendations = pd.Series(user_scores, index=user_movie_matrix.index).sort_values(ascending=False)
    top_recommendations = recommendations.head(top_n)
    return top_recommendations

# Simple command-line interface
while True:
    user_id = int(input("Enter your user ID (or -1 to exit): "))
    if user_id == -1:
        break

    if user_id not in user_movie_matrix.index:
        print("User not found. Please enter a valid user ID.")
    else:
        recommendations = get_movie_recommendations(user_id)
        print(f"Top 10 movie recommendations for User {user_id}:")
        print(recommendations)
