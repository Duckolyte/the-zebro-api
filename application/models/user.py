from application.models.base import BaseModel
from .. import db
from .. import ma


class User(BaseModel):
    first_name = db.Column(db.String(255))
    second_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    date_of_birth = db.Column(db.DateTime(timezone=True))
    missions = db.relationship('Mission', backref='mission', lazy=True)
    user_name = db.Column(db.String(255))  # TODO should be nullable=False when the auth feature is implemented
    email = db.Column(db.String(255))  # TODO should be nullable=False when the auth feature is implemented
    password = db.Column(db.String(255))  # TODO should be nullable=False when the auth feature is implemented


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'created_at', 'created_by', 'update_at', 'updated_by', 'userId', 'parcSection', 'timeStamp')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
