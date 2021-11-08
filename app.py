import pymongo
import flask
from flask import jsonify, request,render_template
import json
client=pymongo.MongoClient('mongodb://mongo:27017/')
client.drop_database('CarRental') #if already present in database ,deleted
mydb=client['CarRental'] #CarRental Database
lcs=mydb.Locations   #Locations collection in CarRental Database
cars=mydb.Car    #Car collection in CarRental Database
drivers=mydb.Driver #Driver collection in CarRental Database
cars.insert_many([{"id":1,"driver":103,"number_plate" : "AP05TZ9909"},
                         {"id" : 1, "driver" : 304, "number_plate" : "TS095555"},
                         { "id" : 3, "driver" : 102, "number_plate" : "AP27PP0098" },
                         {"id" : 4, "driver" : 403, "number_plate" : "TS086754" }]);
drivers.insert_many([{"id" : 102, "name" : "John", "contact" : "9080706050" },
                     {"id" : 103, "name" : "Sai kumar", "contact" : "9998997654" },
                     {"id" : 304, "name" : "koteswarao", "contact" : "7654398765" },
                     {"id" : 403, "name" : "katuri", "contact" : "8899056765" }]);
lcs.insert_many([{"car_id" : 2, "loc" : { "type" : "Point", "coordinates" : [ 25.223804, 55.28456 ] } },
                 {"car_id" : 1, "loc" : { "type" : "Point", "coordinates" : [ 25.197233, 55.274147 ] } },
                 {"car_id" : 3, "loc" : { "type" : "Point", "coordinates" : [ 20.593683, 78.962883 ] } },
                 { "car_id" : 4, "loc" : { "type" : "Point", "coordinates" : [ 24.297243, 55.583146 ]}}] );
lcs.create_index( [( "loc" , "2dsphere" )] );

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False
@app.route('/') #base route
def home():
    return render_template("home.html") #home.html which should present in same locatoin
app.config['JSON_SORT_KEYS'] = False   #to get in unsorted order
@app.route("/location", methods=['GET']) #GET API
def location():
    lat=float(request.args.get("lat")) #taking inputs
    lon=float(request.args.get("long"))
    result=lcs.find({
           'loc': { '$near': {
               '$geometry': {
                  "type": 'Point' ,
                  'coordinates': [ lat , lon ]
               },
             }
           }
        }).limit(3); #return object of top3 nearest locations
    new_l=[]
    for i in result: #accesing every object in result cursor in dictionary form
        d={} #empty dictionary
        r=cars.find({"id":i["car_id"]})  #finding in the cars collection with the car_id of result dictionay
        for j in r:#loop over car cursor object
            driv=drivers.find({"id":j["driver"]}) #find the matching id of driver
            for k in driv: #loop over dirv cursor object
                d["id"]=j["id"]
                d["driver"]=int(k["id"])
                d["number_plate"]=j["number_plate"]
                d["latitude"]=i["loc"]["coordinates"][0]
                d["longitude"]=i["loc"]["coordinates"][1]
                new_l.append(d) #list of dictionaries
    return jsonify(new_l) #converts in to json and return
            
if __name__=="__main__":
    app.run(debug=True)   #running app

