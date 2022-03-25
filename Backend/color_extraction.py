from collections import Counter
from turtle import pen
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tinydb import TinyDB, Query # -> document oriented db
db = TinyDB('colors.json')


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
def analyze(img):
    clf = KMeans(n_clusters = 5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels) # number of extracted colors
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    plt.figure(figsize = (12, 8))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)

    #plt.savefig("results/my_pie2.png")
    print("Found the following colors:\n")

    for color in hex_colors:
      print(color)

    for color in ordered_colors:
        print(color[0])


# filling database
def data():
    db.insert({'name': 'Vihan', 'age': '22'})
    db.insert({'name': 'Dilan', 'age': '29'})
    db.insert({'name': 'Yvonne', 'age': '55'})
    db.insert({'name': 'Sarath', 'age': '61'})

db.drop_tables() # flush the db first
data() # add data to the json file

modified_image = preprocess(image)
analyze(modified_image)
print(db.all())