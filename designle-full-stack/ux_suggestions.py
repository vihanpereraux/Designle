import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report
import sys



def get_features(data):
    importatant_features = []
    for i in range(0, data.shape[0]):
        importatant_features.append(data['design_usage'][i] + ' ' + data['color_category'][i] + ' ' + data['color_usage'][i] + ' ' + data['ux_suggestion'][i])

    return importatant_features


def match_ux_suggestions(user_feedback) :
    suggestions = []
    df = pd.read_csv('data/ux_suggestions.csv', encoding='cp1252') # Getting the data

    columns = ['ux_suggestion', 'color_usage', 'color_category', 'design_usage'] # list of important columns

    # checking whether important columns are filled or not
    if (df[columns].isnull().values.any()) == False:
        
        df['importatant_features'] = get_features(df)  # new coloumn to hold the combined strings

        cm = CountVectorizer().fit_transform(df['importatant_features'])  # convert the text to a matrix

        cs = cosine_similarity(cm)  # getting cosine similarity

        # suggestion = 'Orange ui components' # get the title of the movie that user likes
        
        for user_choice in user_feedback:  
            suggestion_id = df[df.design_usage == user_choice]['suggestion_id'].values[0]  # getting the releavnt movie ID
                
            scores = list(enumerate(cs[suggestion_id]))  # creates a list of enums

            sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)  # sorting the list
            
            k = 1 
            for suggestion in sorted_scores:
                    if k < 5:
                        print('Suggetion - ' , df[df.suggestion_id == suggestion[0]]['design_usage'].values[0])
                        suggestions.append( (df[df.suggestion_id == suggestion[0]]['ux_suggestion'].values[0], df[df.suggestion_id == suggestion[0]]['design_category'].values[0]) )
                        print('Similarity score - ' , suggestion[1]*100,'%', suggestion[0])
                        print('--------------------------------------------------------------------------')
                        k = k + 1

    return(suggestions)


