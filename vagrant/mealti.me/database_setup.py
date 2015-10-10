import sys
from sqlalchemy import Column, ForeignKey, Integer, Float, Boolean, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    popularity = Column(Integer)
    long = Column(Float)
    lat = Column(Float)
    operatingHours = Column(String(91))
    address = Column(String(250))

class User(Base):
    __tablename__ = 'user'

    name = Column(String, nullable = False)
    id = Column(Integer, primary_key = True)
    friends = Column(String)              # format: id1, id2, id3, ...
    favRestaurants = Column(String)       # same as above, only with restaurant ids
    available = Column(Boolean)

class Party(Base):
    __tablename__ = 'party'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    people = Column(String, nullable = False)
    timeRange = Column(String(5), nullable = False)

class Invitation(Base):
    __tablename__ = 'invitation'

    id = Column(Integer, primary_key = True)
    timeRange = Column(String(5), ForeignKey('party.timeRange'))
    sender_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    recepient_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    resaurant_ids = Column(String, nullable = False)

    party = relationship(Party)
    sender = relationship(User, foreign_keys = [sender_id])
    recepient = relationship(User, foreign_keys = [recepient_id])


engine = create_engine('sqlite:///mealtime.db')
Base.metadata.create_all(engine)
