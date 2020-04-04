from application.models.base import BaseModel
from .. import db


class Observation(BaseModel):
    spotId = db.Column(db.String(255), db.ForeignKey('spot.id'), nullable=False)
    animalName = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    age = db.Column(db.String(255))
    pregnancyGrade = db.Column(db.String(255))


class Animal(BaseModel):
    dummy_todo_model = db.Column(db.String(255))
