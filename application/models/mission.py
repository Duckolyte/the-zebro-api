from application.models.base import BaseModel
from .. import db


class Mission(BaseModel):
    userId = db.Column(db.String(255), db.ForeignKey('user.id'))  # TODO in the future should be nullable false
    parcSection = db.Column(db.String(255))
    timeStamp = db.Column(db.DateTime)
    spots = db.relationship('Spot', backref='mission', lazy=True)

    def to_string(self):
        return 'Mission: {id}, {parcSection}, {timeStamp}'.format(
            id=self.id, parcSection=self.parcSection, timeStamp=self.timeStamp
        )
