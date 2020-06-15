from sqlalchemy import Integer, Column, String, Float, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker


Base = declarative_base()

class State(Base):
    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    state_name = Column(String, unique=True)

    def __repr__(self):
        return "<State(state_name='%s')>" % (self.state_name)


class County(Base):
    __tablename__ = 'County'
    id = Column(Integer, primary_key=True)
    county_name = Column(String)
    majority_white = Column(Float)
    state = relation("State", backref = "County")
    state_id = Column(Integer, ForeignKey('State.id'))


# class ComponentCommit(db.Model):
#     __tablename__ = 'component_version'
#     __table_args__ = (
#         db.UniqueConstraint('component_id', 'commit_id', name='unique_component_commit'),
#     )
#     id = db.Column(db.Integer, primary_key=True)
#     component_id = db.Column(db.Integer, db.ForeignKey("component.id"))
#     commit_id = db.Column(db.String)
#     branch = db.Column(db.String)
#     dependencies = db.Column(db.Text)
#     created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     updated_date = db.Column(db.DateTime)


    def __repr__(self):
        return "<County(county_name='%s')>" % (self.county_name)



# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('sqlite:///counties.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()