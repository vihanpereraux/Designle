from doctest import FAIL_FAST
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Getting the data
df = pd.read_csv('data/movies.csv')

# list of important columns
columns = ['Film', 'Genre', 'Audience score %']

# checking whether important columns are filled or not
if (df[columns].isnull().values.any()) == False:
    def get_features(data):
        importatant_features = []
        for i in range(0, data.shape[0]):
            importatant_features.append(data['Film'][i] + ' ' + data['Genre'][i] + ' ' + str(data['Audience score %'][i]))

        return importatant_features
    
    # new coloumn to hold the combined strings
    df['importatant_features'] = get_features(df)

    # convert the text to a matrix
    cm = CountVectorizer().fit_transform(df['importatant_features'])

    # fetting cosine similarity
    cs = cosine_similarity(cm)

    # get the title of the movie that user likes
    title = 'Letters to Juliet'
    
    # getting the releavnt movie ID
    movie_id = df[df.Film == title]['Movie_id'].values[0]
    
    # creates a list of enums
    scores = list(enumerate(cs[movie_id]))

    # sorting the list
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
    sorted_scores = sorted_scores[1:]

    k = 1
    for movie in sorted_scores:
        movie_title = df[df.Movie_id == movie[0]]['Film'].values[0]
        print(movie_title, " - ", movie[0])
        k = k + 1 ;
        if k > 10:
            break
  
