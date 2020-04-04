import json

from application.utils import Serializer
from .. import db


class Mission(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    parcSection = db.Column(db.String(255))
    timeStamp = db.Column(db.DateTime)
    spots = db.relationship('Spot', backref='mission', lazy=True)

    def to_string(self):
        return 'Mission: {id}, {parcSection}, {timeStamp}'.format(
            id=self.id, parcSection=self.parcSection, timeStamp=self.timeStamp
        )

    def to_json(self):
        return json.dumps(self, cls=Serializer)
