# <h1 align="center"> CarRenatal</h1>
---
## How to run the Code?
---
### 1.Download files
### 2.Install Mongodb
* a. Create Database
* b. Add Collections and fill data
### 3.Install Python modules
### 4.Run Location.py
### 5.Open Web Browser
---
## 1. Download files
 Download the Location.py and Home.html from the gituhub repository [CarRental](https://github.com/Gangadhar454/CarRental) <br />
 Store the Two files in same location /same folder
## 2.Install Mongodb
 Download Mongod for your respective Operating using the link [Mongo](https://www.mongodb.com/try/download/community) and Install in your PC <br />
 **Open your Mongo shell** <br />
 (If you are using windows , change director to the bin folder of Mongodb using **Cd Path** and type **mongo** ,then you are into mongo shell)
 ### **a.Create Database**
 Type **Use CarRental** in mongoshell <br />
 Then database with name CarRental will be created
 ### **b. Add Collections and fill data***
 Type the below commands
 * db.Car.insert([{"id":1,"driver":103,"number_plate" : "AP05TZ9909"},{"id" : 1, "driver" : 304, "number_plate" : "TS095555"},
{ "id" : 3, "driver" : 102, "number_plate" : "AP27PP0098" },
{"id" : 4, "driver" : 403, "number_plate" : "TS086754" }]);
* db.Driver.insert([{"id" : 102, "name" : "John", "contact" : "9080706050" },
{"id" : 103, "name" : "Sai kumar", "contact" : "9998997654" },
{"id" : 304, "name" : "koteswarao", "contact" : "7654398765" },
{"id" : 403, "name" : "katuri", "contact" : "8899056765" }]);
* db.Locations.insert([{"car_id" : 2, "loc" : { "type" : "Point", "coordinates" : [ 25.223804, 55.28456 ] } },
{"car_id" : 1, "loc" : { "type" : "Point", "coordinates" : [ 25.197233, 55.274147 ] } },
{"car_id" : 3, "loc" : { "type" : "Point", "coordinates" : [ 20.593683, 78.962883 ] } },
{ "car_id" : 4, "loc" : { "type" : "Point", "coordinates" : [ 24.297243, 55.583146 ] } }]); <br /> <br />
OR you can fill using the json files in the CarRental folder .Refer this [link](https://docs.mongodb.com/database-tools/mongoimport/) to know how to import
## 3.Install Python modules
Open your cmd or shell and Change directory to the python foleder which contain pip files <br />
Type these commands to install modules
* pip install flask
* pip install pymongo
* pip install json

## 4.Run Location.py
   Run the Location.py using your machine <br />
   In the console it will show you a http address [http://127.0.0.1:5000/](http://127.0.0.1:5000/)<br />
   Copy the address
## 5.Open Web Browser
   After opening the Web Browser paste the URL in the search bar <br />
   Two forms will appear on page i.e latitude and longitude <br />
   Enter the details which are in floats<br />
   Click on Search<br />
   The Required output (The nearest top 3 locations of cars)
   
   
   

 
 
 
