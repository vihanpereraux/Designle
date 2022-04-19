from flask import Flask, render_template
import os
from ux_suggestions import match_ux_suggestions

app = Flask(__name__)

@app.route("/")
def home():
    # data = match_ux_suggestions("Orange ui components")
    return render_template("home.html")

@app.route("/about")
def about():
    return "This is about"

if __name__ == '__main__':
    app.run(debug=True)