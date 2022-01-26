from app import db
from flask import render_template, redirect, url_for, Blueprint, abort, send_file
from flask_login import current_user, login_required
from application.forms import MainForm
from application.models import LinkModel, VisitModel
from datetime import datetime, timedelta
import segno
import humanize

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    form = MainForm()
    message = False
    if form.validate_on_submit():
        res = LinkModel.query.filter_by(code=form.code.data).first()
        if res and res.date_expiry < datetime.now():
            message = f'Sorry, the code "{form.code.data}" is already in use.'
        else:
            cid = current_user.id if current_user.is_authenticated else -1
            delta = form.expire.data
            dt = datetime.now()
            if res:
                db.session.delete(res)
            db.session.add(LinkModel(link=form.link.data, code=form.code.data, id=cid,
                                     date_created=dt, date_expiry=dt+delta))
            db.session.commit()
            return redirect(url_for('main.confirmation', code=form.code.data))
    return render_template('main/index.html', form=form, message=message, title="LNK", user=current_user)


@main.route('/dashboard')
@login_required
def dashboard():
    result = LinkModel.query.filter_by(id=current_user.id).all()
    for lnk in result:
        lnk.age = humanize.naturaltime(datetime.now() - lnk.date_created)
    return render_template('main/dashboard.html', rows=result, title=f"LNK Dashboard", user=current_user)


@main.route("/dashboard/<code>")
def confirmation(code):
    if not LinkModel.query.filter_by(code=code).first():
        abort(404)
    count = VisitModel.query.filter_by(code=code).count()
    qr = segno.make_qr("http://www.lnker.me/" + code)
    return render_template('main/confirmation.html', code=code, count=count, title=f"LNK Dashboard | {code}",
                           user=current_user, qr=qr)


@main.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html', title=f"LNK Profile", user=current_user)


@main.route("/static/qr/<code>.png")
def qr_img(code):
    return send_file(f"./static/qr/{code}.png", mimetype='image/png')


@main.route("/404")
@main.errorhandler(404)
def four_oh_four(e):
    return render_template('base/404.html', title="404 Error")


@main.route("/410")
@main.errorhandler(410)
def four_oh_ten(e):
    return render_template('base/410.html', title="410 Error")


@main.route("/<code>")
def redirect_code(code):
    # TODO: add verification for user
    res = LinkModel.query.filter_by(code=f'{code}').first()
    if not res:
        abort(404)
    elif res and res.date_expiry < datetime.now():
        abort(410)
    visit = VisitModel(code=res.code, date=datetime.now())
    db.session.add(visit)
    db.session.commit()
    return redirect(res.link)
