from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms import ValidationError

import app.models as models
from app import db

class Login(FlaskForm):
    username = StringField('username', [validators.DataRequired()])

    def validate_username(form, field):
        value = field.data
        if db.session.query(models.User).filter_by(username=value).first() is None:
            raise ValidationError('user {} not exist'.format(value))


class Register(FlaskForm):
    username = StringField('username', [validators.DataRequired()])

    def validate_username(form, field):
        value = field.data
        if db.session.query(models.User).filter_by(username=value).first() is not None:
            raise ValidationError('user {} yet exist'.format(value))
