# from json import load
# import re
# import os
# from ux_suggestions import match_ux_suggestions
from urllib.parse import uses_fragment
from flask import Flask, flash, redirect, render_template, request, jsonify
from color_extraction import extract_color_features
from ux_suggestions import match_ux_suggestions

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
    results = extract_color_features(img_path)

    return render_template("suggestions.html", content = results)
    
@app.route("/feedback", methods=['POST'])
def feedback():
    user_feedback = request.form.getlist('mymultiselect')
    suggestions = match_ux_suggestions(user_feedback)
    return render_template("suggestions.html", content2 = suggestions)

@app.route("/about")
def about():
    return "This is about"

if __name__ == '__main__':
    app.run(debug=True)