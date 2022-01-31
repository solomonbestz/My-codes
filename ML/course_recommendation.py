import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


#Store the data
df = pd.read_csv('ML/movie-data.csv')
# print(df.head(3))

#Get a count of the number of rows/movies in the data set
print(df.shape)

#Create a list of important columns for the recommendation engine
columns = ['Actors', 'Director', 'Genre', 'Title']

#Show the important data
print(df[columns].head(3))

