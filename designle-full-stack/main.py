from flask import Flask, redirect, render_template, request, jsonify
import flask
from color_extraction import extract_color_features
from ux_suggestions import match_ux_suggestions


from tinydb import TinyDB, Query
db = TinyDB('db.json')

app = Flask(__name__)


@app.route("/")
def home():
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
    db.truncate()
    for item in suggestions:
        db.insert(
            {
                'suggestion': item[0],
                'category': item[1]
            }
        )
    return render_template("results.html", content2 = suggestions)


@app.route("/about")
def aboutz():
    return render_template("about.html")
    

@app.route("/about", methods=['POST'])
def about():
    back = db.all()
    arr = []
    for i in back:
        arr.append(i)
    # print(arr)
    # return str(arr)
    return flask.jsonify({'data': [arr]})    


if __name__ == '__main__':
    app.run(debug=True)