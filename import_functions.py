from model import State, County, dbconnect
import csv
from sqlalchemy import exc

def addData(session, data_input):
    try:
        state = session.query(State).filter(State.state_name == data_input["State"]).one()
    except:
        state = State()
        state.state_name = data_input["State"]
        session.add(state)
    try:
        county = County()
        county.county_name = data_input["County"]
        county.majority_white = data_input["Ethnicities.White Alone, not Hispanic or Latino"]
        county.state = state
        session.add(county)
        session.commit()
        return "OK"
    except exc.IntegrityError:
        session.rollback()
        return "already exists", 400


def import_data(filename):
    return_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return_list.append(dict(row))
    return return_list

session=dbconnect()

imported_counties = import_data("county_demographics.csv")

for row in imported_counties:
    addData(session, row)
# inputs for addData are (session, data_input). The order assures that row is taken as the data_input, not necessary to assign elsewhere
