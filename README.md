# Advanced-Data-Analysis-with-SQLAlchemy-Flask

The project is to analysis the climate change around Hawaii area.

Step 1 - Data Engineering
The climate data for Hawaii is provided through two CSV files clean_hawaii_measurements.csv, and clean_hawaii_stations.csv. 

Step 2 - Database Engineering
Use SQLAlchemy to model the table schemas and create a hawaii.sqlite database for the tables 

Step 3 - Climate Analysis and Exploration
Use Python and SQLAlchemy to do basic climate analysis and data exploration on the  weather station tables. All of the following analysis are completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
Precipitation Analysis
•	Design a query to retrieve the last 12 months of precipitation data.

Station Analysis
•	Design a query to calculate the total number of stations.
•	Design a query to find the most active stations.
•	Design a query to retrieve the last 12 months of temperature observation data.

 
Temperature Analysis
 
Calculate the daily normals. Normals are the averages for min, avg, and max temperatures.
o	Function daily_normals calculates the daily normals for a specific date. The date string is in the format %m-%d.
o	Use Pandas to plot an area plot for the daily normals.
 
________________________________________
Step 4 - Climate App
The Flask api based on the queries for the routes.
Routes
•	/api/v1.0/precipitation
o	Query for the dates and temperature observations from the last year.
o	Convert the query results to a Dictionary using date as the key and tobs as the value.
o	Return the json representation of the dictionary.
•	/api/v1.0/stations
o	Return a json list of stations from the dataset.
•	/api/v1.0/tobs
o	Return a json list of Temperature Observations (tobs) for the previous year
•	/api/v1.0/<start> and /api/v1.0/<start>/<end>
o	Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
o	When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
o	When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.




