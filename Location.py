import pymongo
import flask
from flask import jsonify, request,render_template
import json
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['CarRental'] #CarRental Database
lcs=mydb.Locations   #Locations collection in CarRental Database
cars=mydb.Car    #Car collection in CarRental Database
drivers=mydb.Driver #Driver collection in CarRental Database
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False
@app.route('/') #base route
def home():
    return render_template("home.html") #home.html which should present in same locatoin
app.config['JSON_SORT_KEYS'] = False   #to get in unsorted order
@app.route("/location", methods=['GET','POST']) #location route

def location():
    if request.method=="POST":
        lat=float(request.form.get("lat")) #Taking input from forms
        lon=float(request.form.get("long"))
        result=lcs.find({
           'loc': { '$near': {
               '$geometry': {
                  "type": 'Point' ,
                  'coordinates': [ lat , lon ]
               },
             }
           }
        }).limit(3); #This will retrurn cursor object of top3 near locations
        new_l=[] #new empty list
        for i in result: #accesing every object in result cursor in dictionary form
            d={}  #empty dictionary
            r=cars.find({"id":i["car_id"]}) #finding in the cars collection with the car_id of result dictionay
            for j in r: #loop over car cursor object
                driv=drivers.find({"id":j["driver"]}) #find the matching id of driver
                for k in driv: #loop over dirv cursor object
                    d["id"]=j["id"]
                    d["driver"]=int(k["id"])    #storing in dictionary with respective keys
                    d["number_plate"]=j["number_plate"]
                    d["latitude"]=i["loc"]["coordinates"][0]
                    d["longitude"]=i["loc"]["coordinates"][1]
                    new_l.append(d) #list of dictionaries
    return jsonify(new_l) #converts in to json and return
if __name__=="__main__":
    app.run(debug=True)   #running app
