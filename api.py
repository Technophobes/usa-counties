import csv
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import dbconnect, State, County
from sqlalchemy import exc

app = Flask(__name__)


@app.route('/state/<search_term>')
def state(search_term):
    return_list = []
    for row in data:
        if row["State"] == "WA":
            return_list.append(row)
    return jsonify(return_list)

@app.route('/majority_white_counties')
def majority_white():
    session = dbconnect()
    


if __name__ == '__main__':
    data = import_data("county_demographics.csv")
    app.run(debug=True)
