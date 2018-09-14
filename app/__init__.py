from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user):
    return models.User(username=user)


from app import views
import app.models as models

app.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
app.add_url_rule('/random', view_func=views.RandomView.as_view('random'))
app.add_url_rule('/history', view_func=views.HistoryView.as_view('history'))


app.add_url_rule('/comein', view_func=views.ComeInView.as_view('comein'))
app.add_url_rule('/new', view_func=views.NewView.as_view('new'))
app.add_url_rule('/logout', view_func=views.LogoutView.as_view('logout'))

if __name__ == '__main__':
    app.run()
