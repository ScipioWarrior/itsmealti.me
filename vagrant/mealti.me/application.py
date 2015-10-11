from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, User, Party, Invitation

engine = create_engine('sqlite:///mealtime.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/start')
def startPage():
    return render_template('start.html')

@app.route('/create-party')
def createParty():
    return render_template('create_party.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
