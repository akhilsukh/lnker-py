from app import db
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from application.forms import MainForm
import datetime
from application.models import LinkModel, VisitModel

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    form = MainForm()
    message = False
    if form.validate_on_submit():
        if LinkModel.query.get(form.code.data):
            message = f'Sorry, the code "{form.code.data}" is already in use.'
        else:
            db.session.add(LinkModel(link=form.link.data, code=form.code.data, date=datetime.datetime.now()))
            db.session.commit()
            return redirect(url_for('confirmation', code=form.code.data))
    return render_template('index.html', form=form, message=message, title="LNK", user=current_user)


@main.route("/dashboard/<code>")
def confirmation(code):
    if not LinkModel.query.filter_by(code=code).first():
        return redirect(url_for('404'))
    count = VisitModel.query.filter_by(code=code).count()
    return render_template('confirmation.html', code=code, count=count, title=f"LNK Dashboard | {code}", user=current_user)


@main.route('/dashboard')
@login_required
def dashboard():
    result = LinkModel.query.all()
    return render_template('dashboard.html', rows=result, title=f"LNK Dashboard", user=current_user)


@main.route("/404")
@main.errorhandler(404)
def four_oh_four(e):
    return render_template('404.html', title="404 Error")


@main.route("/<code>")
def redirect_code(code):
    # TODO: add verification for user
    link = LinkModel.query.filter_by(code=f'{code}').first()
    if not link:
        return redirect(url_for('404'))
    visit = VisitModel(code=link.code, date=datetime.datetime.now())
    db.session.add(visit)
    db.session.commit()
    return redirect(link.link)
