from application.models.base import BaseModel
from .. import db
from .. import ma


class Mission(BaseModel):
    userId = db.Column(db.String(255), db.ForeignKey('user.id'))  # TODO in the future should be nullable false
    parcSection = db.Column(db.String(255))
    timeStamp = db.Column(db.DateTime)
    spots = db.relationship('Spot', backref='mission', lazy=True)


class MissionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'created_at', 'created_by', 'update_at', 'updated_by', 'userId', 'parcSection', 'timeStamp')


mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)
