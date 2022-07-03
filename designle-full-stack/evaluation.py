from collections import Counter
from sklearn.cluster import KMeans
import cv2
import math
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

from sklearn.metrics.cluster import rand_score
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import fowlkes_mallows_score


def extract_color_features(img_path):
        
    # importing and color correction process
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # resizing and pre-processing the image
    image = cv2.resize(image, (900, 600), interpolation = cv2.INTER_LINEAR)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3) # keeps the aspect ratio of the resized image according to the original image

    # analyzing the image
    num_of_colors = 1
    clf = KMeans(n_clusters = num_of_colors)
    color_labels = clf.fit_predict(image) # cluster collection -> lots of 0s,1s and 2s
    center_colors = clf.cluster_centers_ # RGB color values belong to clusters | After performing clustering, the cluster centers can be extracted via .cluster_centers_.
    # https://scikit-learn-general.narkive.com/2113zSYN/interpreting-the-cluster-centers-in-sklearn-kmeans
    counts = Counter(color_labels) # amounts of three cluster collections
    print(center_colors)

    # adding RGB values into an array
    extracted_colors = []
    for i in range(num_of_colors):
        extracted_colors.append(center_colors[i])

    # color channel calculations relate to the domain
    sRGB_versions = []    
    channel_contribution = []
    for color in extracted_colors :
        sRGB_versions.append(sRGBColor(color[0], color[1], color[2]))

    for color in sRGB_versions :
        color_LAB = convert_color(color, LabColor)

        if color_LAB.lab_a < 0 :
            color_LAB_achannel = int(round(math.sqrt(color_LAB.lab_a * -1), 0) * -1)
        else :
            color_LAB_achannel = int(round(math.sqrt(color_LAB.lab_a), 0))

        if color_LAB.lab_b < 0 :
            color_LAB_bchannel = int(round(math.sqrt(color_LAB.lab_b * -1), 0) * -1)
        else :
            color_LAB_bchannel = int(round(math.sqrt(color_LAB.lab_b), 0))

        if color_LAB.lab_l < 0 :
            color_LAB_lchannel = int(round(math.sqrt(color_LAB.lab_l * -1), 0) * -1)
        else :
            color_LAB_lchannel = int(round(math.sqrt(color_LAB.lab_l), 0))

        channel_contribution.append((color_LAB_achannel, color_LAB_bchannel, color_LAB_lchannel))


    # Identifying color ranges of extracted colors 
    color_features = []

    for feature in channel_contribution :
        # if -6 < color_LAB_achannel < 6  and -6 < color_LAB_bchannel < 6 :
        # color sceheme 01
        if 70 <= feature[0] <= 80 and feature[1] >= 70 : 
            color_features.append( ("Red") )
        if 30 <= feature[0] <= 69 and 0 <= feature[1] <= 70 :
            color_features.append( ("Red shades") )

        if 80 <= feature[0] and -80 <= feature[1] <= -10 : 
            color_features.append("Purple")
        if 40 <= feature[0] <= 80 and -80 <= feature[1] <= -10 : 
            color_features.append("Purple shades")
            
        if 30 <= feature[0] <= 70 and 40 <= feature[1] : 
            color_features.append("Orange")
        if 20 <= feature[0] <= 40 and 30 <= feature[1] : 
            color_features.append("Orange shades")


        # color sceheme 02
        if 60 <= feature[1] <= 100 and (-40 <= feature[0] <= 0 or 0 <= feature[0] <= 40) : 
            color_features.append("Yellow")
        if 30 <= feature[1] <= 60 and (-40 <= feature[0] <= 0 or 0 <= feature[0] <= 40) : 
            color_features.append("Yellow shades")

        if 30 <= feature[1] <= 100 and -100 <= feature[0] <= -50 : 
            color_features.append("Green")
        if 30 <= feature[1] <= 100 and -50 <= feature[0] <= -30 : 
            color_features.append("Green shades")

        if -100 <= feature[1] <= -50 and 60 <= feature[0] <= 100 : 
            color_features.append("Blue")
        if -50 <= feature[1] <= -30 and (0 <= feature[0] <= 60 or -60 <= feature[0] <= 0) : 
            color_features.append( "Blue shades" )
        if -100 <= feature[1] <= -50 and (0 <= feature[0] <= 60 or -60 <= feature[0] <= 0) : 
            color_features.append( "Blue shades" )
            

        # color sceheme 03
        if -25 <= feature[1] <= 25 and -25 <= feature[0] <= 25 :
            color_features.append("Black")
            color_features.append("Black shades")

        if -6 < color_LAB_achannel < 6  and -6 < color_LAB_bchannel < 6 :
            # part of color sceheme 03
            color_features.append("White shades")


    print("l", color_LAB_lchannel)
    print("a", color_LAB_achannel)
    print("b", color_LAB_bchannel)
    print("Color features", color_features)


# extract_color_features('test/scheme 02/average/blue 03.png')


# scheme 01 evalution
scheme01_labels_true = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
scheme01_labels_pred = [1, 1, 0, 2, 2, 0, 2, 3, 3, 0]

scheme01_rand_score = rand_score(scheme01_labels_true, scheme01_labels_pred)
scheme01_adjusted_rand_score = adjusted_rand_score(scheme01_labels_true, scheme01_labels_pred)
scheme01_normalized_mutual_info_score = normalized_mutual_info_score(scheme01_labels_true, scheme01_labels_pred)
scheme01_fowlkes_mallows_score = fowlkes_mallows_score(scheme01_labels_true, scheme01_labels_pred)

# print("Scheme 01 rand score", scheme01_rand_score)
# print("Scheme 01 adjusted rand score", scheme01_adjusted_rand_score)
# print("Scheme 01 normalized mutual info score", scheme01_normalized_mutual_info_score)
# print("Scheme 01 fowlkes mallows score", scheme01_fowlkes_mallows_score)


scheme02_labels_true = [4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
scheme02_labels_pred = [4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 2]

scheme02_rand_score = rand_score(scheme02_labels_true, scheme02_labels_pred)
scheme02_adjusted_rand_score = adjusted_rand_score(scheme02_labels_true, scheme02_labels_pred)
scheme02_normalized_mutual_info_score = normalized_mutual_info_score(scheme02_labels_true, scheme02_labels_pred)
scheme02_fowlkes_mallows_score = fowlkes_mallows_score(scheme02_labels_true, scheme02_labels_pred)

print("Scheme 02 rand score", scheme02_rand_score)
print("Scheme 02 adjusted rand score", scheme02_adjusted_rand_score)
print("Scheme 02 normalized mutual info score", scheme02_normalized_mutual_info_score)
print("Scheme 02 fowlkes mallows score", scheme02_fowlkes_mallows_score)





