import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    """List all Routes that are Available"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Retrieve last 12 mos. of precipitation data"""
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    sel = [Measurement.date, Measurement.prcp]
    
    session = Session(engine)
    
    results = session.query(*sel).\
    filter(Measurement.date >= prev_year).all()
    
    session.close()

    prev_precip = []
    for date, prcp in results:
        precip_dict = {}
        #need to determine first of all if i should use that session query 
            #above to do last 12 mos. or if it's all the datapoints for prcp
        #precip_dict["name"] = name
        #passenger_dict["age"] = age
        #passenger_dict["sex"] = sex
        #all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


    return 






if __name__=="__main__"
    app.run(debug=True)