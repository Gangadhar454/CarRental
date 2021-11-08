## GET API using Flask Framework
---
```python
import flask
from flask import jsonify, request,render_template
import json
app = flask.Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
```
First, we are importing the flask module into our application and then defining the API route. The @ is used for defining the API route. We’re passing /, which means this is our base route.It will return the render template home.html which is present in the same location as location.py
#### To Run the server and Making API CALL
To run the server, execute the below command:
```
flask run
```
#### Another Route
```python
from flask import jsonify, request,render_template
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
```
Here, we have imported some more modules from Flask, like request,jsonify and render_template. We are using request to get the data which the user is sending, and we’re using jsonify for converting dictionaries to JSON. We have added one more route that is /location it will return a json.

**Now once again head over to the API testing tool and hit URL:**
http://127.0.0.1:5000/

