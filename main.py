from flask import Flask, render_template, json, request
from pprint import pprint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/testband')
def testband():
    my_dict = { "title": "Gunship", "genre": "Synthwave"}
    return json.dumps(my_dict)

@app.route('/testalbums', methods=['POST'])
def testalbums():
    my_dict = { 0: "Gunship", 1: "Dark All Day"}
    pprint(request.json)
    return json.dumps(my_dict)

if __name__ == "__main__":
    app.run(debug=True)
