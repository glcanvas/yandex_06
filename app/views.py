import json
import random

from flask.views import View
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user

from app import db

import app.models as models

from app.forms import Login
from app.forms import Register


class LoginView(View):
    methods = ['GET']

    def dispatch_request(self):
        if current_user.is_authenticated:
            return render_template('login.html')
        else:
            register_form = Register()
            login_form = Login()
            register_errors = json.loads(session.get('new-user', '{}'))
            login_errors = json.loads(session.get('come-in-user', '{}'))
            session.pop('new-user', None)
            session.pop('come-in-user', None)
            return render_template('login.html', register_form=register_form, login_form=login_form,
                                   register_errors=register_errors, login_errors=login_errors)


class ComeInView(View):
    methods = ['POST']

    def dispatch_request(self):
        form = Login(request.form)
        if form.validate_on_submit():
            user = db.session.query(models.User).filter_by(username=form.username.data).first()
            login_user(user)
            return redirect(url_for('login'))
        session['come-in-user'] = json.dumps(form.errors)
        return redirect(url_for('login'))


class NewView(View):
    methods = ['POST']

    def dispatch_request(self):
        form = Register(request.form)
        if form.validate_on_submit():
            usr = models.User(username=form.username.data)
            db.session.add(usr)
            db.session.commit()
            user = db.session.query(models.User).filter_by(username=form.username.data).first()
            login_user(user)
            return redirect(url_for('login'))
        session['new-user'] = json.dumps(form.errors)
        return redirect(url_for('login'))


class LogoutView(View):
    methods = ['POST']

    def dispatch_request(self):
        logout_user()
        return redirect(url_for('login'))


class RandomView(View):
    methods = ['GET']

    def dispatch_request(self):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        value = random.randint(0, 100)
        number = models.Number(number=value, user_id=current_user.username)
        db.session.add(number)
        db.session.commit()
        return render_template('random.html', value=value)


class HistoryView(View):
    methods = ['GET']

    def dispatch_request(self):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        numbers = db.session.query(models.User).filter_by(id=current_user.username).first().numbers
        numbers = list(map(lambda x:x.number, numbers))
        return render_template('history.html', numbers=numbers)