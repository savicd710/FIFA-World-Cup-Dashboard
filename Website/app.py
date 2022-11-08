import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, redirect


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../database/fifa_data.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
CountryData = Base.classes.country_data
MatchData = Base.classes.match_data
SquadData = Base.classes.squad_data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    print('Welcome')
    return render_template('main_view.html')

@app.route("/api/v1.0/country_data")
def country_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all country data"""
    # Query all countries
    results = session.query(CountryData.team).all()

    session.close()

    # Convert list of tuples into normal list
    all_countries = list(np.ravel(results))

    return jsonify(all_countries)

@app.route("/api/v1.0/match_data")
def match_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all match data"""
    # Query all countries
    results = session.query(MatchData.date, MatchData.home_team, MatchData.home_team_fifa_rank).all()

    session.close()
    
    # Create a dictionary from the row data and append to a list of all_ranks
    all_ranks = []
    for date, home_team, home_team_fifa_rank in results:
        rank_dict = {}
        rank_dict["date"] = date
        rank_dict["home_team"] = home_team
        rank_dict["home_team_fifa_rank"] = home_team_fifa_rank
        all_ranks.append(rank_dict)

    return jsonify(all_ranks)

@app.route("/api/v1.0/squad_data")
def squad_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all squad data"""
    # Query all countries
    results = session.query(SquadData.year, SquadData.country, SquadData.age).all()

    session.close()

    all_squad = []
    for year, country, age in results:
        squad_dict = {}
        squad_dict["year"] = year
        squad_dict["country"] = country
        squad_dict["age"] = age
        all_squad.append(squad_dict)

    return jsonify(all_squad)














if __name__ == '__main__':
    app.run(debug=True)