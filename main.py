from flask import Flask, render_template, json, request
from pprint import pprint
from os import listdir

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/testband')
def testband():
    my_dict = { "title": "The Midnight", "genre": "Synthwave"}
    return json.dumps(my_dict)

@app.route('/testalbums', methods=['POST'])
def testalbums():
    band = request.json['params']['band'];
    if band == "Gunship":
    	albums = ["Gunship", "Dark All Day"]
    elif band == "The Midnight":
    	albums = ["Days of Thunder", "Endless Summer", "Nocturnal", "Kids"]

    print(albums)
    return json.dumps(albums)

@app.route('/getInputImageFilenames')
def getInputImageFilenames():
    return json.dumps(listdir(app.root_path + "/static/img/input"))

if __name__ == "__main__":
    app.run(debug=True)
