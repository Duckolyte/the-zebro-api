from application.models.base import BaseModel
from .. import db
from .. import ma


class Spot(BaseModel):
    missionId = db.Column(db.String(255), db.ForeignKey('mission.id'), nullable=False)
    observationQualityCode = db.Column(db.String(255))
    observationDateTime = db.Column(db.DateTime(timezone=True))
    observations = db.relationship('Observation', backref='spot', lazy=True)
    gps = db.relationship('GpsPoint', backref='spot', lazy=True)


class SpotSchema(ma.Schema):
    class Meta:
        fields = ('id', 'created_at', 'created_by', 'update_at', 'updated_by', 'userId', 'parcSection', 'timeStamp')


spot_schema = SpotSchema()
spots_schema = SpotSchema(many=True)


class GpsPoint(BaseModel):
    spotId = db.Column(db.String(255), db.ForeignKey('spot.id'), nullable=False)
    x = db.Column(db.String(255))
    y = db.Column(db.String(255))


class GpsPointSchema(ma.Schema):
    class Meta:
        fields = ('id', 'created_at', 'created_by', 'update_at', 'updated_by', 'spotId', 'x', 'y')


gps_point_schema = SpotSchema()
gps_points_schema = SpotSchema(many=True)
