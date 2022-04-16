import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report
import sys

from matplotlib import pyplot as plt
import seaborn as sns


def get_features(data):
    importatant_features = []
    for i in range(0, data.shape[0]):
        importatant_features.append(data['design_usage'][i] + ' ' + data['color_category'][i] + ' ' + data['color_usage'][i] + ' ' + data['ux_suggestion'][i])

    return importatant_features


def match_ux_suggestions(suggestion) :
    # df = pd.read_csv('data/ux_suggestions.csv', encoding='cp1252', skiprows=0, nrows=70)
    df = pd.read_csv('data/ux_suggestions.csv', encoding='cp1252') # Getting the data

    columns = ['ux_suggestion', 'color_usage', 'color_category', 'design_usage'] # list of important columns

    # checking whether important columns are filled or not
    # if (df[columns].isnull().values.any()) == False:
        
    # new coloumn to hold the combined strings
    df['importatant_features'] = get_features(df)
    print(df.head(3));

    # convert the text to a matrix
    cm = CountVectorizer().fit_transform(df['importatant_features'])

    # getting cosine similarity
    cs = cosine_similarity(cm)

    # get the title of the movie that user likes
    # suggestion = 'Orange ui components'
        
    # getting the releavnt movie ID
    suggestion_id = df[df.design_usage == suggestion]['suggestion_id'].values[0]
        
    # creates a list of enums
    scores = list(enumerate(cs[suggestion_id]))

    # sorting the list
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
    # sorted_scores = sorted_scores[1:]
    
    # k = 1 
    # for suggestion in sorted_scores:
    #         if k < 6:
    #             print('Suggetion - ' , df[df.suggestion_id == suggestion[0]]['design_usage'].values[0])
    #             print('Similarity score - ' , suggestion[1]*100,'%', suggestion[0])
    #             print('--------------------------------------------------------------------------')
    #             k = k + 1

    return(sorted_scores)
# match_ux_suggestions()


# def test_accuracy() :
#     df = pd.read_csv('data/ux_suggestions.csv', encoding='cp1252')
#     df['importatant_features'] = get_features(df)
#     cm = CountVectorizer().fit_transform(df['importatant_features'])
#     cs = cosine_similarity(cm)

#     basic_colorz = ["Red", "Purple", "Orange", "Yellow", "Blue", "Green"]
#     # prediction = ["Red shades", "Purple", "Orange", "Yellow", "Blue", "Green"]
#     arara = []
#     bvbvbv = []
#     true_usages = ["Orange backgrounds", "Orange ui components", "Red ui components", "Blue ui components", "Bright blue backgrounds", "Yellow ui components"]
    
#     for usage in true_usages :
#         acc_usage = usage
#         suggestion_id = df[df.design_usage == acc_usage]['suggestion_id'].values[0]
#         scores = list(enumerate(cs[suggestion_id]))
#         sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)

#         arara.append( ((df[df.suggestion_id == sorted_scores[0][0]]['design_usage'].values[0]),(df[df.suggestion_id == sorted_scores[1][0]]['design_usage'].values[0]),(df[df.suggestion_id == sorted_scores[2][0]]['design_usage'].values[0])) )
#         # for i in range(3):
#             # arara.append( (df[df.suggestion_id == sorted_scores[i][0]]['design_usage'].values[0]) )
    
#     for ddd in arara :
#         if( true_usages[0][0] in ddd[0] and true_usages[0] == ddd[1] and true_usages[0] == ddd[2] ) :
#             bvbvbv.append(true_usages[0])
#     print(arara)

# test_accuracy()





    # cm = confusion_matrix(truth, prediction)
    # print_confusion_matrix(cm,["Dog","Not a dog"])
    # print(cm,["Red", "Purple", "Orange", "Yellow", "Blue", "Green"])
    # print(classification_report(truth, prediction))

