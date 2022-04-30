from json import load
from flask import Flask, flash, redirect, render_template, request
import os
from ux_suggestions import match_ux_suggestions
from color_extraction import read_img

app = Flask(__name__)

@app.route("/")
def home():
    # data = match_ux_suggestions("Orange ui components")
    return render_template("home.html")

@app.route("/suggestions", methods=['GET'])
def suggestions():
    return render_template("suggestions.html")

@app.route("/suggestions", methods=['POST'])
def extract_colors():
    img_file = request.files['file']
    img_path = "./images/" + img_file.filename
    img_file.save(img_path)
    read_img(img_path)

    return render_template("suggestions.html")
    

@app.route("/about")
def about():
    return "This is about"

if __name__ == '__main__':
    app.run(debug=True)