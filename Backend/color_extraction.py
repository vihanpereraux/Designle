from collections import Counter
from itertools import count
from turtle import pen
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2

from tinydb import TinyDB, Query # -> document oriented db
db = TinyDB('database/colors.json')

from colormath.color_objects import AdobeRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


# Importing and color correction process
image = cv2.imread('images/Image01.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Resizing and pre-processing the image
def preprocess(raw):
    image = cv2.resize(raw, (900, 600), interpolation = cv2.INTER_NEAREST)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3) # keeps the aspect ratio of the resized image according to the original image
    return image


# Converting rgb to hex
def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color


# Analyzing the image
def extract_colors(img):
    clf = KMeans(n_clusters = 3)
    color_labels = clf.fit_predict(img) # cluster collection -> lots of 0s,1s and 2s
    center_colors = clf.cluster_centers_ # RGB color values belong to clusters
    counts = Counter(color_labels) # amounts of three cluster collections

    # adding RGB values into an array
    extracted_rgb_colors = []
    for i in counts.keys():
        extracted_rgb_colors.append(center_colors[i])

    data(extracted_rgb_colors)


# filling the database with hex values
def data(extracted_rgb_data):
    if len(extracted_rgb_data) != 0:
        db.drop_tables() # flush the db first
        for data in extracted_rgb_data:
            db.insert({ 'hexValues': rgb_to_hex(data) })
    else:
        print('Colors are not available')
    
    color_calculations(extracted_rgb_data)


# Danger and comfort color calculations
def color_calculations(rgb_colors):
    LAB_colors = []
    for color in rgb_colors:
        rgb_color = AdobeRGBColor(color[0], color[1], color[2])
        LAB_colors.append(convert_color(rgb_color, LabColor))
    
    print(len(LAB_colors))


preprocessed_image = preprocess(image)
extract_colors(preprocessed_image)

#color_calculations()

