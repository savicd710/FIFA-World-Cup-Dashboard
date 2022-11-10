import numpy as np
import pandas as pd

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
    squad_results = session.query(SquadData.country, SquadData.year, SquadData.age, SquadData.caps).all()
    session.close()

    squad_data = []
    for country, year, age, caps in squad_results:
        dict = {}
        dict["country"] = country
        dict["year"] = year
        dict["age"] = age
        dict["caps"] = caps
        squad_data.append(dict)
    
    squad_data_pd = pd.DataFrame(squad_data)
    squad_data_pd.caps = squad_data_pd.caps.str.extract('(\d+)').dropna().astype('int64')
    squad_data_pd.dropna(inplace=True)

    heat_data = squad_data_pd.groupby(['country', 'year']).mean()
    heat_data = heat_data.reset_index(level=0)
    heat_data = heat_data.reset_index(level=0)

    caps = list(heat_data.caps)
    teams = list(heat_data.country)
    years = list(heat_data.year)
    age = list(heat_data.age)

    return render_template('team_view.html', squad_data=squad_data, caps = caps, teams = teams, years = years, age = age)

@app.route("/rating_view")
def rating_view():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all rating data"""
    # Query all data
    results = session.query(MatchData.date,MatchData.home_team_fifa_rank, MatchData.away_team_fifa_rank, MatchData.tournament, MatchData.winner).all()
    session.close()

    match_data = []
    for date, better_ea_team_win, better_fifa_team_win, tournament in results:
        dict = {}
        dict["date"] = date
        dict["home_team"] = home_team
        dict["away_team"] = away_team
        dict["home_team_rank"] = home_team_rank
        dict["away_team_rank"] =away_team_rank
        dict["tournament"] = tournament
        dict["winner"] = winner
        match_data.append(dict)

    return render_template('rating_view.html', data=match_data, date= date,home_team = home_team, away_team = away_team, home_team_rank = home_team_rank, away_team_rank = away_team_rank, tournament = tournament, winner = winner)

@app.route("/map_view")
def map_view():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all map data"""
    # Query all data
    results = session.query(CountryData.date, CountryData.team, CountryData.tournament, CountryData.cup_year, CountryData.lat, CountryData.long).filter(CountryData.tournament == 'FIFA World Cup').all()
    session.close()

    country_data = []
    for date, team, tournament, cup_year, lat, long in results:
        dict = {}
        dict["date"] = date
        dict["team"] = team
        dict["tournament"] = tournament
        dict["cup_year"] = cup_year
        dict["lat"] = lat
        dict["long"] = long
        country_data.append(dict)

    return render_template('map_view.html', data=country_data)

@app.route("/api/map_data")
def map_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all map data"""
    # Query all data
    results = session.query(CountryData.date, CountryData.team, CountryData.tournament, CountryData.cup_year, CountryData.lat, CountryData.long).filter((CountryData.tournament == 'FIFA World Cup')).all()
    session.close()

    country_data = []
    for date, team, tournament, cup_year, lat, long in results:
        dict = {}
        dict["date"] = date
        dict["team"] = team
        dict["tournament"] = tournament
        dict["cup_year"] = cup_year
        dict["lat"] = lat
        dict["long"] = long
        country_data.append(dict)
    
    return jsonify(country_data)



if __name__ == '__main__':
    app.run(debug=True)
