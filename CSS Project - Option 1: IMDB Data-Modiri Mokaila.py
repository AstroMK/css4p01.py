#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:29:34 2024

@author: user
"""


#CLEANING THE DATA
import pandas as pd
movies = pd.read_csv("/home/user/Documents/School 2024/CHPC 2024/movie_dataset.csv")
Movies = pd.read_csv("/home/user/Documents/School 2024/CHPC 2024/movie_dataset1.csv") #This is the original dataset without the edits

#Remove rows with NAN values
movies.dropna(subset=['Revenue (Millions)', 'Metascore'], inplace=True)

#Question 1: What is the highest rated movie in the dataset?
movies["Rating"].max() # This looks for the row with highest Rating 
highest_rate = movies[movies["Rating"] == movies["Rating"].max()]
print("The highest rated movie in the dataset: ", highest_rate)

#Question 2: What is the average revenue of all movies in the dataset? 
avg_rev = movies['Revenue (Millions)'].mean()
print("The average revenue of all movies in the dataset: ", avg_rev)

#Question 3: What is the average revenue of movies from 2015 to 2017 in the dataset?
#Select all rows where Year = 2015, 2016 and 2017
years = movies[(movies["Year"] >= 2015) & (movies["Year"] <= 2017)]
print("The average revenue of movies from 2015 to 2017 in the dataset: ", years["Revenue (Millions)"].mean())


#Question 4: How many movies were released in the year 2016?
year = Movies[Movies["Year"] == 2016]
print("The number of movies released in the year 2016: ", len(year))


#Question 6: How many movies in the dataset have a rating of at least 8.0?
movies_rate = Movies[Movies["Rating"] >= 8.0]
print("The number of movies in the dataset have a rating of at least 8.0: ", len(movies_rate))

#Question 5: How many movies were directed by Christopher Nolan?
CN = movies[movies["Director"] == 'Christopher Nolan']
print("The Number of movies were directed by Christopher Nolan: ", len(CN))

#Question 7: What is the median rating of movies directed by Christopher Nolan?
movies_CN_Med = CN["Rating"].median()
print("The median rating of movies directed by Christopher Nolan: ", movies_CN_Med)

#Question 8: Find the year with the highest average rating?
group_year = movies.groupby('Year')["Rating"].mean()
print("The year with the highest average rating appears in this list: ", group_year)

#Question 9: What is the percentage increase in number of movies made between 2006 and 2016?
num_movies = movies[(movies["Year"] > 2006) & (movies["Year"] < 2016)]
num_mov1 = len(movies[movies["Year"] == 2006]) #Number of movies made in 2006
num_mov2 = len(movies[movies["Year"] == 2016]) #Number of movies made in 2016
per_inc = ((num_mov2-num_mov1)/num_mov1)*100
print("The percentage increase in number of movies made between 2006 and 2016: ", per_inc)

#Question 10: Find the most common actor in all the movies?
num_actors = movies["Actors"].str.split(', ', expand=True).stack()
num_actors_count = num_actors.value_counts()
common_actor = num_actors_count.idxmax()
print("The most common actor in all the movies: ", common_actor)

#Question 11: How many unique genres are there in the dataset?
genres = Movies["Genre"].str.split(', ', expand=True).stack().unique()
num_genres = len(genres)
print("The number of unique genres are there in the dataset: ", num_genres)







