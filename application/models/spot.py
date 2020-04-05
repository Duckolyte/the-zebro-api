from application.models.base import BaseModel
from .. import db
from .. import ma


class Spot(BaseModel):
    missionId = db.Column(db.String(255), db.ForeignKey('mission.id'))  # TODO in the future should be nullable false
    observationQualityCode = db.Column(db.String(255))
    observationDateTime = db.Column(db.DateTime(timezone=True))
    gps = db.relationship('GpsPoint', backref='spot', lazy=True)
    observations = db.relationship('Observation', backref='spot', lazy=True)


class SpotSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'created_at',
                  'created_by',
                  'modified_at',
                  'modified_by',
                  'missionId',
                  'observationQualityCode',
                  'observationDateTime')


spot_schema = SpotSchema()
spots_schema = SpotSchema(many=True)


class GpsPoint(BaseModel):
    spotId = db.Column(db.String(255), db.ForeignKey('spot.id'), nullable=False)
    lat = db.Column(db.String(255))
    lon = db.Column(db.String(255))


class GpsPointSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'created_at',
                  'created_by',
                  'modified_at',
                  'modified_by',
                  'spotId',
                  'lat',
                  'lon')


gps_point_schema = SpotSchema()
gps_points_schema = SpotSchema(many=True)
