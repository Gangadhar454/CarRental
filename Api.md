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
```
Here, we have imported some more modules from Flask, like request,jsonify and render_template. We are using request to get the data which the user is sending, and we’re using jsonify for converting dictionaries to JSON. We have added one more route that is /location and also passing POST as a list and returning back what the user is sending in the parameters.

**Now once again head over to the API testing tool and hit URL:**
http://127.0.0.1:5000/

