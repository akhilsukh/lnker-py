import os
from app import app, db
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from application.forms import MainForm
import datetime

from application.models import LinkModel, VisitModel


@app.route("/", methods=['GET', 'POST'])
def index():
    form = MainForm()
    message = False
    if form.validate_on_submit():
        if LinkModel.query.get(form.code.data):
            message = True
        else:
            message = False
            lm = LinkModel(link=form.link.data, code=form.code.data, date=datetime.datetime.now())
            db.session.add(lm)
            db.session.commit()
            return redirect(url_for('confirmation', code=form.code.data))
    return render_template('index.html', form=form, message=message, title="LNK")


@app.route("/dashboard/<code>")
def confirmation(code):
    return render_template('confirmation.html', code=code, title=f"LNK Dashboard | {code}")


@app.route('/dashboard')
def dashboard():
    result = LinkModel.query.all()
    return render_template('dashboard.html', rows=result, title=f"LNK Dashboard")


@app.route("/404")
@app.errorhandler(404)
def four_oh_four(e):
    return render_template('404.html', title="404 Error")


@app.route("/<code>")
def redirect_code(code):
    # TODO: add verification for user
    link = LinkModel.query.filter_by(code=f'{code}').first()
    if not link:
        return redirect(url_for('404'))
    # insert into visits table
    visit = VisitModel(code=link.code, date=datetime.datetime.now())
    db.session.add(visit)
    db.session.commit()
    return redirect(link.link)
