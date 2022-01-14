import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from application.forms import MainForm
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cT13FYw7nMowrpsBQBc29zwWhlBZL5j7'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:postgres@localhost:5432/lnk')\
    .replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application.routes import *


@app.cli.command('create_db')
def create_db():
    db.create_all()
    db.session.commit()
