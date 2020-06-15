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
    __table_args__ = (
        UniqueConstraint('state_id', 'county_name', name='unique_county_state'),
    )
    id = Column(Integer, primary_key=True)
    county_name = Column(String)
    majority_white = Column(Float)
    state = relation("State", backref = "County")
    state_id = Column(Integer, ForeignKey('State.id'))


    def __repr__(self):
        return "<County(county_name='%s')>" % (self.county_name)



# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('sqlite:///counties.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()