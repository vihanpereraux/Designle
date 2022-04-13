from collections import Counter
from sklearn.cluster import KMeans
import cv2
import math
from tinydb import TinyDB, Query # -> document oriented db
db = TinyDB('database/colors.json')
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


# importing and color correction process
image = cv2.imread('images/Design03.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# resizing and pre-processing the image
def preprocess(raw):
    image = cv2.resize(raw, (900, 600), interpolation = cv2.INTER_LINEAR)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3) # keeps the aspect ratio of the resized image according to the original image
    return image


# converting rgb to hex
def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color


# analyzing the image
def extract_colors(img):
    clf = KMeans(n_clusters = 3)
    color_labels = clf.fit_predict(img) # cluster collection -> lots of 0s,1s and 2s
    center_colors = clf.cluster_centers_ # RGB color values belong to clusters
    counts = Counter(color_labels) # amounts of three cluster collections

    # adding RGB values into an array
    extracted_colors = []
    for i in range(3):
        extracted_colors.append(center_colors[i])

    calculate_channel_contribution(extracted_colors)


# color channel calculations relate to the domain
def calculate_channel_contribution(extracted_colors):
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

        channel_contribution.append((color_LAB_achannel, color_LAB_bchannel))
    
    # print(channel_contribution)
    identify_color_ranges(channel_contribution)


# Identifying color ranges of extracted colors 
def identify_color_ranges(channel_contribution):
    color_features = []

    # color sceheme 01
    for feature in channel_contribution :
        if 70 <= feature[0] <= 80 and feature[1] >= 70 : 
            color_features.append("Red")
        if 30 <= feature[0] <= 69 and 0 <= feature[1] <= 70 :
            color_features.append("Red shades")

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
        if 0 <= feature[1] <= 60 and (-40 <= feature[0] <= 0 or 0 <= feature[0] <= 40) : 
            color_features.append("Yellow shades")

        if 0 <= feature[1] <= 100 and -100 <= feature[0] <= -50 : 
            color_features.append("Green")
        if 0 <= feature[1] <= 100 and -50 <= feature[0] <= 0 : 
            color_features.append("Green shades")

        if -100 <= feature[1] <= -50 and 60 <= feature[0] <= 100 : 
            color_features.append("Blue")
        if -50 <= feature[1] <= 0 and (0 <= feature[0] <= 60 or -60 <= feature[0] <= 0) : 
            color_features.append("Blue shades")
        if -100 <= feature[1] <= -50 and (0 <= feature[0] <= 60 or -60 <= feature[0] <= 0) : 
            color_features.append("Blue shades")

    for i in range(3):
        print(color_features[i])


preprocessed_image = preprocess(image)
extract_colors(preprocessed_image)
# calculate_channel_contribution( [(255, 0, 0), (131, 188, 118), (249, 216)] )


















# def data(extracted_rgb_data):

#     if len(extracted_rgb_data) != 0:
#         db.drop_tables() # flush the db first
#         for data in extracted_rgb_data:
#             db.insert({ 'hexValues': rgb_to_hex(data) })
#     else:
#         print('Colors are not available')
    
#     print(extracted_rgb_data)



# from collections import Counter
# from itertools import count
# import py_compile
# from turtle import pen
# from sklearn.cluster import KMeans
# from matplotlib import colors
# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
# import math

# from tinydb import TinyDB, Query # -> document oriented db
# db = TinyDB('database/colors.json')

# from colormath.color_objects import sRGBColor, LabColor
# from colormath.color_conversions import convert_color
# from colormath.color_diff import delta_e_cie2000
