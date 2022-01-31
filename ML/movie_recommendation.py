import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#Store the data
df = pd.read_csv('ML/movie-data.csv')

# Updating the cvv with movie id ranging from 0 - the end of moie
df['Movie_Id'] = range(0, 1000)
 
#Create a list of important columns for the recommendation engine
columns = ['Actors', 'Director', 'Genre', 'Title']

#Show the important data
df[columns].head(3)

#check for any missing value in the important columns
is_empty = df[columns].isnull().values.any()


# Create a function to combine the values of the important columns into a single string
def get_important_features(datas):
    important_features = []
    for i in range(0, datas.shape[0]):
        important_features.append(f"{datas['Actors'][i]}  {datas['Director'][i]}  {datas['Genre'][i]}  {datas['Title'][i]}")
    return important_features

# Create a column to hold the combined strings
df['Important_features'] = get_important_features(df)

# Show the data
# print(df.head(3))


# Convert the text to a matrix of token counts
cm = CountVectorizer().fit_transform(df['Important_features'])

#Get the cosine similarity matrix from the count matrix
cs = cosine_similarity(cm)

#print the cosine similarity matrix
# print(cs)

#get the shape of the cosine similarity matrix
# print(cs.shape)

#Get the title of the movie that the user likes
title = "Trolls"

#Find the movies id
movie_id = df[df.Title == title]['Movie_Id'].values[0]

#Create a list of enumerations for the similarity score [(movie_id, similarity score), ]
scores = list(enumerate(cs[movie_id]))

#Sort the list /// we are sorting on the similarity score using lambda ///
sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
sorted_scores = sorted_scores[1:]

#print the sorted scores
# print(sorted_scores)


#Create a loop to print the first 7 similar movies
j = 0
print('THe seven most recommended movies to', title, 'are:\n')
for item in sorted_scores:
    movie_title = df[df.Movie_Id == item[0]]['Title'].values[0]
    print(j+1, movie_title)
    j += 1
    if j > 6:
        break




