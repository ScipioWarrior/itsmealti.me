from flask import Flask, render_template
application = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, User, Party, Invitation

engine = create_engine('sqlite:///mealtime.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@application.route('/')
@application.route('/start')
def startPage():
    return render_template('start.html')

@application.route('/create-party')
def createParty():
    return render_template('create_party.html')

@application.route('/restaurants')
def showRestaurant():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants = restaurants)


if __name__ == "__main__":
    application.debug = True
    application.run()
