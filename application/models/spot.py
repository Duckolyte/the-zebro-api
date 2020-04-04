from application.models.base import BaseModel
from .. import db


class Spot(BaseModel):
    missionId = db.Column(db.String(255), db.ForeignKey('mission.id'), nullable=False)
    observationQualityCode = db.Column(db.String(255))
    observationDateTime = db.Column(db.DateTime(timezone=True))
    observations = db.relationship('Observation', backref='spot', lazy=True)
    gps = db.relationship('GpsPoint', backref='spot', lazy=True)


class GpsPoint(BaseModel):
    gpsId = db.Column(db.String(255), db.ForeignKey('spot.id'), nullable=False)
    x = db.Column(db.String(255), unique=True, nullable=False)
    y = db.Column(db.String(255), unique=True, nullable=False)
