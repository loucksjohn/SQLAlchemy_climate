# sqlalchemy-challenge

In this repository for the SQLAlchemy Homework, you will find my ##Climate Analysis and Exploration (Step 1) 
contained in the Jupyter notebook entitled "climate_starter.ipynb", and the ##Climate App (Step 1) in the file 
entitled "app.py".  

For Step 1, the starter notebook provided some amount of boilerplate code....importing of libraries/modules/etc.  
So first step was to create engine variable that would allow for connection to the "Hawaii.sqlite" database.  Following 
the creation of the "create_engine", I used the automap_base to reflect the tables into classes.  I also used DB Browser
for SQLite just open up the "Hawaii.sqlite" database and see what the tables were & what kind of data they containted.

On the the precipitation analysis.  After doing an initial query to determine most recent date in the database, I used 
that date (2017-08-23) and the datetime function of timedelta to create a variable for the timeframe of "the last 12 months.
Once I had that, and another variable containing the classes I wanted to query, i did a session.query to get all the 
recorded rainfall for the previous year and put it into a DataFrame (rainfall_df).  With that DataFrame I could then plot the data into
a bar chart:</br>
![alt text](https://github.com/loucksjohn/sqlalchemy-challenge/blob/main/rainfall_bar.png?raw=true)

After that it was time to run a query to find the most how active each weather station had been over the timeframe of that dataset, 
there were 9 total stations.  The query that I ran for that one was a little more complicated as it involved doing a .group_by & 
.order_by in order to get the results that i wanted. After determining which station was the most active,I could then look at highest 
temp. recorded, avg. temp, and lowest temp.  All that was left to do then was to pull the last twelve months of temp data for most active
station (USC00519281) and plot a histogram from the results: ![alt text](https://github.com/loucksjohn/sqlalchemy-challenge/blob/main/station_hist.png?raw=true)