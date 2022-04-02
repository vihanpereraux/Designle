import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Getting the data
df = pd.read_csv('data/ux_suggestions.csv', encoding='cp1252')
# print(df.head(11));

# list of important columns
columns = ['ux_suggestion', 'usage', 'category']


# checking whether important columns are filled or not
if (df[columns].isnull().values.any()) == False:
    def get_features(data):
        importatant_features = []
        for i in range(0, data.shape[0]):
            importatant_features.append(data['ux_suggestion'][i] + ' ' + data['usage'][i] + ' ' + data['category'][i])

        return importatant_features
    
    # new coloumn to hold the combined strings
    df['importatant_features'] = get_features(df)
    # print(df.head(3));

    # convert the text to a matrix
    cm = CountVectorizer().fit_transform(df['importatant_features'])

    # getting cosine similarity
    cs = cosine_similarity(cm)

    # get the title of the movie that user likes
    suggestion = 'Red always makes you feel that you are running out of time and rushes you to take the next action.'
    
    # getting the releavnt movie ID
    suggestion_id = df[df.ux_suggestion == suggestion]['suggestion_id'].values[0]
    
    # creates a list of enums
    scores = list(enumerate(cs[suggestion_id]))

    # sorting the list
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
    # sorted_scores = sorted_scores[1:]

    # k = 1
    for suggestion in sorted_scores:
        ux_suggestions = df[df.suggestion_id == suggestion[0]]['ux_suggestion'].values[0]
        print(sorted_scores)
        print('---------------------------------------------------------------------------')
        # k = k + 1 ;
        # if k > 10:
        #     break


  
