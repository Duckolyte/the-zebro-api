from .. import db


class Observation(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    spotId = db.Column(db.String(255), db.ForeignKey('spot.id'), nullable=False)
    animalName = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    age = db.Column(db.String(255))
    pregnancyGrade = db.Column(db.String(255))


class Animal(db.Model):
    id = db.Column(db.String(255), primary_key=True)
