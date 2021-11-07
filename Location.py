import pymongo
import flask
from flask import jsonify, request,render_template
import json
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['CarRental']
lcs=mydb.Locations
cars=mydb.Car
drivers=mydb.Driver
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False
@app.route('/')
def home():
    return render_template("home.html")
app.config['JSON_SORT_KEYS'] = False
@app.route("/location", methods=['GET','POST'])

def location():
    if request.method=="POST":
        lat=float(request.form.get("lat"))
        lon=float(request.form.get("long"))
        result=lcs.find({
           'loc': { '$near': {
               '$geometry': {
                  "type": 'Point' ,
                  'coordinates': [ lat , lon ]
               },
             }
           }
        }).limit(3);
        new_l=[]
        for i in result:
            d={}
            r=cars.find({"id":i["car_id"]})
            for j in r:
                driv=drivers.find({"id":j["driver"]})
                for k in driv:
                    d["id"]=j["id"]
                    d["driver"]=int(k["id"])
                    d["number_plate"]=j["number_plate"]
                    d["latitude"]=i["loc"]["coordinates"][0]
                    d["longitude"]=i["loc"]["coordinates"][1]
                    new_l.append(d)
    return jsonify(new_l)
if __name__=="__main__":
    app.run(debug=True)
