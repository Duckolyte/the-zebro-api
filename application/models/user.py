from application.models.base import BaseModel
from .. import db
from .. import ma


class User(BaseModel):
    first_name = db.Column(db.String(255))
    second_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    date_of_birth = db.Column(db.DateTime(timezone=True))
    user_name = db.Column(db.String(255))  # TODO should be nullable=False when the auth feature is implemented
    email = db.Column(db.String(255))  # TODO should be nullable=False when the auth feature is implemented
    password = db.Column(db.String(255))  # TODO should be nullable=False when the auth feature is implemented
    missions = db.relationship('Mission', backref='mission', lazy=True)

    def __init__(self, first_name, second_name, last_name, date_of_birth, user_name, email, password, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.user_name = user_name
        self.email = email
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'created_at',
                  'created_by',
                  'modified_at',
                  'modified_by',
                  'first_name',
                  'second_name',
                  'last_name',
                  'date_of_birth',
                  'user_name',
                  'email',
                  'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
