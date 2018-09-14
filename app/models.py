from app import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    numbers = db.relationship('Number', backref='user', lazy=True)

    def __repr__(self):
        return "{}".format(self.username)


class Number(db.Model):
    __tablename__ = 'number'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


db.create_all()
