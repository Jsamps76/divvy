from app import db



class Divvy(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime)
    stoptime = db.Column(db.DateTime)
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String(45))
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String(45))
    usertype = db.Column(db.String(45))
    gender = db.Column(db.String(45))
    birthday = db.Column(db.String(45))
    trip_duration = db.Column(db.Integer)

    def to_json(self):
        return {'trip_id': self.trip_id, 'duration': self.trip_duration}
