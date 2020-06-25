from model import dbconnect, State, County, dbconnect
from sqlalchemy import exc

def add_county_from_queue(request_dict):
    session = dbconnect()
    try:
        state_instance = session.query(State).filter(State.id == request_dict["state_id"]).one()
    except:
        # wrong
        return "State does not exist, please add it", 400

    try:
        county = County()
        county.county_name = request_dict["County"]
        county.majority_white = request_dict["Ethnicities.White Alone, not Hispanic or Latino"]
        county.state = state_instance
        session.add(county)
        session.commit()
        # removed json below because this is for flask
        return county.id

    except exc.IntegrityError:
        session.rollback()
        # wrong
        return "already exists", 400