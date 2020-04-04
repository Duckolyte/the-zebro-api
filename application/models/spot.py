from .. import db


class Spot(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    missionId = db.Column(db.String(255), db.ForeignKey('mission.id'), nullable=False)
    observationQualityCode = db.Column(db.String(255))
    observationDateTime = db.Column(db.DateTime(255))
    observations = db.relationship('Observation', backref='spot', lazy=True)
    gps = db.relationship('GpsPoint', backref='spot', lazy=True)


class GpsPoint(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    gpsId = db.Column(db.String(255), db.ForeignKey('spot.id'), nullable=False)
    x = db.Column(db.String(255), unique=True, nullable=False)
    y = db.Column(db.String(255), unique=True, nullable=False)
