import csv
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import dbconnect, State, County
from sqlalchemy import exc
from import_functions import import_data

app = Flask(__name__)


@app.route('/state/<search_term>')
def state(search_term):
    return_list = []
    for row in data:
        if row["State"] == search_term:
            return_list.append(row)
    return jsonify(return_list)


# return a list of counties from that state that have a majority of white people and returns all demogrphic data
@app.route('/state/<search_term>/majority_white_counties')
def majority_white(search_term):
    return_list = []
    for row in data:
        if row["State"] == search_term:
            if row["Ethnicities.White Alone, not Hispanic or Latino"] > "50":
                return_dict = {
                    "County":row["County"], 
                    "Ethnicities.White Alone, not Hispanic or Latino": row["Ethnicities.White Alone, not Hispanic or Latino"], 
                    "Ethnicities.American Indian and Alaska Native Alone": row["Ethnicities.American Indian and Alaska Native Alone"], 
                    "Ethnicities.Asian Alone": row["Ethnicities.Asian Alone"], 
                    "Ethnicities.Black Alone": row["Ethnicities.Black Alone"], 
                    "Ethnicities.Hispanic or Latino": row["Ethnicities.Hispanic or Latino"], 
                    "Ethnicities.Native Hawaiian and Other Pacific Islander Alone": row["Ethnicities.Native Hawaiian and Other Pacific Islander Alone"], 
                    "Ethnicities.Two or More Races": row["Ethnicities.Two or More Races"], 
                    "Ethnicities.White Alone": row["Ethnicities.White Alone"] 
                    }
                return_list.append(return_dict)
                
    return jsonify(return_list)
    

@app.route('/<search_term_1>/<search_term_2>')
def county_ethnicities(search_term_1, search_term_2):
    return_list = []
    for row in data:
            if row["State"] == search_term_1:
                if row["Ethnicities.White Alone, not Hispanic or Latino"] > search_term_2:
                    return_dict = {
                        "County":row["County"], 
                        "Ethnicities.White Alone, not Hispanic or Latino": row["Ethnicities.White Alone, not Hispanic or Latino"], 
                        "Ethnicities.American Indian and Alaska Native Alone": row["Ethnicities.American Indian and Alaska Native Alone"], 
                        "Ethnicities.Asian Alone": row["Ethnicities.Asian Alone"], 
                        "Ethnicities.Black Alone": row["Ethnicities.Black Alone"], 
                        "Ethnicities.Hispanic or Latino": row["Ethnicities.Hispanic or Latino"], 
                        "Ethnicities.Native Hawaiian and Other Pacific Islander Alone": row["Ethnicities.Native Hawaiian and Other Pacific Islander Alone"], 
                        "Ethnicities.Two or More Races": row["Ethnicities.Two or More Races"], 
                        "Ethnicities.White Alone": row["Ethnicities.White Alone"] 
                        }
                    return_list.append(return_dict)
                
    return jsonify(return_list)



if __name__ == '__main__':
    data = import_data("county_demographics.csv")
    app.run(debug=True)
