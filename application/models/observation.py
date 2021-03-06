from application.models.base import BaseModel
from .. import db
from .. import ma


class Observation(BaseModel):
    spotId = db.Column(db.String(255), db.ForeignKey('spot.id'))  # TODO in the future should be nullable false
    animalName = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    age = db.Column(db.String(255))
    pregnancyGrade = db.Column(db.String(255))


class ObservationSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'created_at',
                  'created_by',
                  'modified_at',
                  'modified_by',
                  'spotId',
                  'animalName',
                  'sex',
                  'age',
                  'pregnancyGrade')


observation_schema = ObservationSchema()
observations_schema = ObservationSchema(many=True)


class Animal(BaseModel):
    dummy_todo_model = db.Column(db.String(255))
