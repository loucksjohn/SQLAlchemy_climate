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
        precip_dict[date] = prcp
               
        prev_precip.append(precip_dict)

    return jsonify(prev_precip)

@app.route("/api/v1.0/stations")
def stations():
    """Retrieve list of stations from Dataset"""
    session = Session(engine)
    station_list = session.query(Station.station, Station.name, Station.latitude, Station.longitude).all()
    session.close()
    all_stations = list(np.ravel(station_list))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Retrieve USC00519281 TOBS for previous year"""
    session = Session(engine)
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    tobs_results = session.query(Measurement.tobs).\
    filter(Measurement.date >= prev_year).\
    filter(Measurement.station == "USC00519281").all()
    session.close()
    results_tobs = list(np.ravel(tobs_results))
    return jsonify(results_tobs)


if __name__ == '__main__':
    app.run(debug=True)

