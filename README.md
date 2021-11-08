# <h1 align="center"> CarRenatal</h1>
---
## How to run the Code?
---
### 1.Download files
### 2.Install Mongodb
### 3.Install Python modules
### 4.Run Location.py
### 5.Open Web Browser
---
## 1. Download files
 Download the Location.py and Home.html from the gituhub repository [CarRental](https://github.com/Gangadhar454/CarRental) <br />
 create a foader called "templates" and store the Home.html file in the holder<br />
 The Location.py and templates folder should be in same location
## 2.Install Mongodb
 Download Mongod for your respective Operating using the link [Mongo](https://www.mongodb.com/try/download/community) and Install in your PC <br />
I have created and fill the database collections using insert function Written in Location.py<br />
There is no need to fill the database manually
## 3.Schema of the Database
**Database Name = CarRental** <br />
There are 3 collections in CarRental Database <br />
* Car <br />
There are 3 fields in every document of Car collection <br />
"id" -> Number <br />
"driver" -> Number <br />
"number_plate" -> String <br />
* Driver
There are 3 fields in every document of Driver collection <br />
"id" -> Number <br />
"name" -> String <br />
"contact" -> String <br />
* Locations
There are two fields in every document of Locations collection <br />
"car_id" -> Number <br />
"loc" -> object it contains a dictionary of key=loc and values dictionary of key="coordinates"and values= array which contain two Point(floats) <br />

## 4.Install Python modules
Open your cmd or shell and Change directory to the python foleder which contain pip files <br />
Type these commands to install modules
* pip install flask
* pip install pymongo
* pip install json

## 5.Run Location.py
   Run the Location.py using your machine <br />
   In the console it will show you a http address [http://127.0.0.1:5000/](http://127.0.0.1:5000/)<br />
   Copy the address
## 6.Open Web Browser
   After opening the Web Browser paste the URL in the search bar <br />
   Two forms will appear on page i.e latitude and longitude <br />
   Enter the details which are in floats<br />
   Click on Search .It will take you to the url http://127.0.0.1:5000/location <br />
   The Required output (The nearest top 3 locations of cars)
   
   
   

 
 
 
