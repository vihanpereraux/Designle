from collections import Counter
from sklearn.cluster import KMeans
import cv2
import math
from tinydb import TinyDB, Query # -> document oriented db
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


def extract_color_features(img_path):
        
    # importing and color correction process
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # resizing and pre-processing the image
    image = cv2.resize(image, (900, 600), interpolation = cv2.INTER_LINEAR)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3) # keeps the aspect ratio of the resized image according to the original image

    # analyzing the image
    clf = KMeans(n_clusters = 3)
    color_labels = clf.fit_predict(image) # cluster collection -> lots of 0s,1s and 2s
    center_colors = clf.cluster_centers_ # RGB color values belong to clusters
    counts = Counter(color_labels) # amounts of three cluster collections


    # adding RGB values into an array
    extracted_colors = []
    for i in range(3):
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
        if color_LAB_lchannel < 85 :
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

        else :
            # part of color sceheme 03
            color_features.append("White shades")

    print("l", color_LAB_lchannel)
    print("a", color_LAB_achannel)
    print("b", color_LAB_bchannel)

    temp = []
    flat_list = []
    for color_feature in color_features:
        temp.append(color_feature.split())
        
    for sublist in temp:
        for item in sublist:
            flat_list.append(item)


    Fruit = Query()
    db = TinyDB('database/design_usages.json')

    design_feature = [] # design usages

    for item in list(dict.fromkeys(flat_list)):
        match item:

            case "Blue":
                blue_usages = []
                for i in range(3):
                    blue_usages.append(db.search(Fruit.basicColor == 'Blue')[0]['usage'+str(i+1)])
                for item in blue_usages:
                    design_feature.append(item)
            
            case "Red":
                red_usages = []
                for i in range(3):
                    red_usages.append(db.search(Fruit.basicColor == 'Red')[0]['usage'+str(i+1)])
                for item in red_usages:
                    design_feature.append(item)
            
            case "Orange":
                orange_usages = []
                for i in range(3):
                    orange_usages.append(db.search(Fruit.basicColor == 'Orange')[0]['usage'+str(i+1)])
                for item in orange_usages:
                    design_feature.append(item)
            
            case "Purple":
                purple_usages = []
                for i in range(2):
                    purple_usages.append(db.search(Fruit.basicColor == 'Purple')[0]['usage'+str(i+1)])
                for item in purple_usages:
                    design_feature.append(item)
            
            case "Green":
                green_usages = []
                for i in range(3):
                    green_usages.append(db.search(Fruit.basicColor == 'Green')[0]['usage'+str(i+1)])
                for item in green_usages:
                    design_feature.append(item)
            
            case "Yellow":
                yellow_usages = []
                for i in range(3):
                    yellow_usages.append(db.search(Fruit.basicColor == 'Yellow')[0]['usage'+str(i+1)])
                for item in yellow_usages:
                    design_feature.append(item)
            
            case "White":
                white_usages = []
                for i in range(2):
                    white_usages.append(db.search(Fruit.basicColor == 'White')[0]['usage'+str(i+1)])
                for item in white_usages:
                    design_feature.append(item)
            
            case "Black":
                black_usages = []
                for i in range(2):
                    black_usages.append(db.search(Fruit.basicColor == 'Black')[0]['usage'+str(i+1)])
                for item in black_usages:
                    design_feature.append(item)
            
            case "Brown":
                brown_usages = []
                for i in range(3):
                    brown_usages.append(db.search(Fruit.basicColor == 'Brown')[0]['usage'+str(i+1)])
                for item in brown_usages:
                    design_feature.append(item)

    return design_feature
