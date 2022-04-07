import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import sys


# Getting the data
# df = pd.read_csv('data/ux_suggestions.csv', encoding='cp1252', skiprows=0, nrows=70)
df = pd.read_csv('data/color_scheme_02.csv', encoding='cp1252')
# print(df.head(1));

# list of important columns
columns = ['ux_suggestion', 'color_usage', 'color_category', 'design_usage']
# print(df['design_usage'][0])
# print(df[columns].isnull().values.any())
# sys.exit()


# checking whether important columns are filled or not
if (df[columns].isnull().values.any()) == False:
    def get_features(data):
        importatant_features = []
        for i in range(0, data.shape[0]):
            importatant_features.append(data['design_usage'][i] + ' ' + data['color_category'][i] + ' ' + data['color_usage'][i] + ' ' + data['ux_suggestion'][i])

        return importatant_features
    
    # new coloumn to hold the combined strings
    df['importatant_features'] = get_features(df)
    print(df.head(3));

    # convert the text to a matrix
    cm = CountVectorizer().fit_transform(df['importatant_features'])

    # getting cosine similarity
    cs = cosine_similarity(cm)

    # get the title of the movie that user likes
    suggestion = 'Yellow ui components'
    
    # getting the releavnt movie ID
    suggestion_id = df[df.design_usage == suggestion]['suggestion_id'].values[0]
    
    # creates a list of enums
    scores = list(enumerate(cs[suggestion_id]))

    # sorting the list
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
    # sorted_scores = sorted_scores[1:]


    k = 1 
    for suggestion in sorted_scores:
        if k < 6:
            print('Suggetion - ' , df[df.suggestion_id == suggestion[0]]['design_usage'].values[0])
            print('Similarity score - ' , suggestion[1]*100,'%', suggestion[0])
            print('--------------------------------------------------------------------------')
            k = k + 1


  
