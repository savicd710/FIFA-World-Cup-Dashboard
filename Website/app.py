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
def welcome():
    """Return the welcome page"""
    return render_template('welcome.html')

@app.route("/main_view")
def main_view():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all country data"""
    # Query all data
    results = session.query(CountryData.date, CountryData.team, CountryData.goals_scored, CountryData.tournament, CountryData.result, CountryData.goal_diff, CountryData.cup_year).all()
    session.close()

    country_data = []
    for date, team, goals_scored, tournament, result, goal_diff, cup_year in results:
        dict = {}
        dict["date"] = date
        dict["team"] = team
        dict["goals_scored"] = goals_scored
        dict["tournament"] = tournament
        dict["result"] = result
        dict["goal_diff"] = goal_diff
        dict["cup_year"] = cup_year
        country_data.append(dict)

    return render_template('main_view.html', data=country_data)

@app.route("/team_view")
def team_view():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all team data"""
    # Query all data
    country_results = session.query(CountryData.date, CountryData.team, CountryData.fifa_rank, CountryData.tournament, CountryData.cup_year).all()
    squad_results = session.query(SquadData.country, SquadData.year, SquadData.age, SquadData.caps).all()
    session.close()

    country_data = []
    for date, team, fifa_rank, tournament, cup_year in country_results:
        dict = {}
        dict["date"] = date
        dict["team"] = team
        dict["fifa_rank"] = fifa_rank
        dict["tournament"] = tournament
        dict["cup_year"] = cup_year
        country_data.append(dict)

    squad_data = []
    for country, year, age, caps in squad_results:
        dict = {}
        dict["country"] = country
        dict["year"] = year
        dict["age"] = age
        dict["caps"] = caps
        squad_data.append(dict)

    return render_template('team_view.html', country_data=country_data, squad_data=squad_data)

@app.route("/rating_view")
def rating_view():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all rating data"""
    # Query all data
    results = session.query(MatchData.date, MatchData.better_ea_team_win, MatchData.better_fifa_team_win, MatchData.tournament).all()
    session.close()

    match_data = []
    for date, better_ea_team_win, better_fifa_team_win, tournament in results:
        dict = {}
        dict["date"] = date
        dict["better_ea_team_win"] = better_ea_team_win
        dict["better_fifa_team_win"] = better_fifa_team_win
        dict["tournament"] = tournament
        match_data.append(dict)

    return render_template('rating_view.html', data=match_data)




if __name__ == '__main__':
    app.run(debug=True)