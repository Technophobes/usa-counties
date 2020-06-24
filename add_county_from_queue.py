from model import dbconnect, State, County, dbconnect
from sqlalchemy import exc

def add_county_from_queue(request_dict):
    session = dbconnect()
    request_dict = request.get_json()
    try:
        state_instance = session.query(State).filter(State.id == request_dict["state_id"]).one()
    except:
        return "State does not exist, please add it", 400

    try:
        county = County()
        county.county_name = request_dict["County"]
        county.majority_white = request_dict["Ethnicities.White Alone, not Hispanic or Latino"]
        county.state = state_instance
        session.add(county)
        session.commit()
        return jsonify(county.id)

    except exc.IntegrityError:
        session.rollback()
        return "already exists", 400