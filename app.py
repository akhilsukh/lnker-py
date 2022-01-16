import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cT13FYw7nMowrpsBQBc29zwWhlBZL5j7'
app.config['SQLALCHEMY_DATABASE_URI'] = os\
    .getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/lnk')\
    .replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

lm = LoginManager(app)
lm.login_view = 'auth.login'

# from application.models import *
from application.models import UserModel


@lm.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))


from application.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from application.main import main as main_blueprint
app.register_blueprint(main_blueprint)


@app.cli.command('create_db')
def create_db():
    db.create_all()
    db.session.commit()
