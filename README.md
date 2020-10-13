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

I did go ahead and do ##Temperature Analysis II bonus portion that was on the starter notebook.  Again, some bootstrapping was provided that 
would do the calculation on the trip dates that I put in.  The bulk of the problem was to figure out how to then plot those results into a
bar chart.  First thing I did was  create a variable for the calc temps so that i could then use the Numpy Ravel function to take the results
out tuple format and into a list format. then it was just a matter of setting up the variables for the tMIN, tAVG, and tMAX so that i could 
plot out the following bar chart: ![alt text](https://github.com/loucksjohn/sqlalchemy-challenge/blob/main/bonus_bar.png?raw=true)

I didn't get to any of the other bonus problems.

The other piece of the assignment was to create a Climate App using a Flask API based on the queries I explained above.  I encourage you to
check out the Flask API i built--i mentioned it earlier, but it's the file entitled "app.py".  Here are the list for all the routes you can
go to in the app:</br>
/api/v1.0/precipitation<br/>
/api/v1.0/stations<br/>
/api/v1.0/tobs<br/>
/api/v1.0/start_only/<start><br/>
/api/v1.0/start_end/<start>/<end><br/>

TWO THINGS I want to point out:  1)for the last two routes, "start_only" and "start_end", the date format needs to be YYYY-MM-DD, 
and 2)you need to have a slash between the start date and the end date for the "start_end" route.  So it would look 
like /api/v1.0/start_end/2016-05-20/2017-05-01.  And the results that are returned for those last two routes are [min. temp, avg. temp, and max. temp].
When given only the start date, it will calc those values for all dates greater than or equal to the date you provide.  And when you 
use the other route and provide a start date and an end date, it will calc the min, avg, max temps for all those dates in between what you provided.

thanks for reading.  Please feel free to reach out if you have any questions or suggested improvements.  This one was alot of fun.  I 
can't wait to get to Hawaii......