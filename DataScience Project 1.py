#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd

ratings_data = pd.read_csv(r'C:\Users\malli\Downloads\imdb_top_1000 - imdb_top_1000.csv.csv')
movie_titles_df = pd.read_csv(r'C:\Users\malli\Downloads\imdb_top_1000 - imdb_top_1000.csv.csv')

average_ratings = ratings_data.groupby('movie_id')['rating'].mean()

sorted_movies = average_ratings.sort_values(ascending=False)

# Specify the range of movies to select (from 100th to 1000th)
start_index = 1 
end_index = 3 

# Get movies within the specified range
selected_movies = sorted_movies.iloc[start_index:end_index+1]

# Calculate the average rating of the selected movies
average_rating_selected = selected_movies.mean()

# Get the top-rated movie within the specified range
top_movie_id = selected_movies.idxmax()
top_movie_title = movie_titles_df[movie_titles_df['movie_id'] == top_movie_id]['title'].values[0]
top_movie_rating = selected_movies.max()

# Get the list of movie titles within the specified range
selected_movie_titles = []
for movie_id in selected_movies.index:
    movie_title = movie_titles_df[movie_titles_df['movie_id'] == movie_id]['title'].values[0]
    selected_movie_titles.append(movie_title)

print(f"Average Rating of Selected Movies: {average_rating_selected:.2f}")
print(f"Title of the Top-Rated Movie: {top_movie_title}")
print(f"Top-Rated Rating: {top_movie_rating:.2f}")
print("List of Movie Titles:")
for title in selected_movie_titles:
    print(title)


# In[ ]:




