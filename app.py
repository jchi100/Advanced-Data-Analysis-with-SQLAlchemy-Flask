#
# Climate app with Flask
# Datasource: hawaii.sqlite
#
import sqlalchemy
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Create an engine to a SQLite database file called `hawaii.sqlite`
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurements
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

# Query for the dates and precipitation values from the last year.
# Convert the query results to a Dictionary using date as the key and tobs as the value.
# Return the json representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date)
    
    # Create a dictionary from the row data and append to a list
    precipitation_list = []
    for result in results:
        precipitation_dict = {}
        precipitation_dict[result.date]= result.prcp
        precipitation_list.append(precipitation_dict)

    return jsonify(precipitation_list)

# Return a json list of stations from the dataset.
    
@app.route("/api/v1.0/stations")
def stations():
   
    results = session.query(Station.name).all()

    station_list = list(np.ravel(results))

    return jsonify(station_list)


# Return a json list of Temperature Observations (tobs) for the previous year
@app.route("/api/v1.0/tobs")
def tobs():

    results = session.query(Measurement.date,Measurement.tobs).all()

    tobs_list = []
    
    for result in results:
        tobs_dict = {}
        tobs_dict[result.date]= result.tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

#Return a json list of the minimum temperature, the average temperature,
# and the max temperature for a given start or start-end range.

@app.route("/api/v1.0/temperatures_query/<start_date>")
def temperatures_query(start_date):
      temperature_result={}
  
      temperature_result['Start Date'] = start_date
      
      results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).all()
    
      
      
      temperature_result['Minimum Temperature'] = results[0][0]
      temperature_result['Average Temperature'] = results[0][1]
      temperature_result['Maximum Temperature'] = results[0][2]
      return jsonify(temperature_result)
      

@app.route("/api/v1.0/temperatures_query/<start_date>/<end_date>")
def temperaturesquery(start_date,end_date):
      
      temperature_result={}
  
      temperature_result['Start Date'] = start_date
      temperature_result['End Date'] = end_date
      results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).\
                filter(Measurement.date <= end_date).all()
      
   
      
      temperature_result['Minimum Temperature'] = results[0][0]
      temperature_result['Average Temperature'] = results[0][1]
      temperature_result['Maximum Temperature'] = results[0][2]
      return jsonify(temperature_result)
      


if __name__ == '__main__':
    app.run(debug=True)