from app import db
from flask import render_template, redirect, url_for, request, flash, Blueprint
from application.forms import LoginForm, SignupForm
from application.models import UserModel
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('dashboard'))
    #     db.session.add(LinkModel(link=form.link.data, code=form.code.data, date=datetime.datetime.now()))
    #     db.session.commit()
    #     return redirect(url_for('confirmation', code=form.code.data))
    return render_template('auth/login.html', form=form, title=f"Login | LNK", user=current_user)


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = UserModel.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=True)
    return redirect(url_for('main.dashboard'))


@auth.route('/signup')
def signup():
    form = SignupForm()
    # if form.validate_on_submit():
    #     user = UserModel.query.filter_by(email=form.email.data)
    #     # if not user:
    #
    #     return redirect(url_for('dashboard'))
    return render_template('auth/signup.html', form=form, title=f"Signup | LNK", user=current_user)


# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    passwordConfirm = request.form.get('passwordConfirm')

    if password != passwordConfirm:
        flash(f"Passwords don't match: {password} != {passwordConfirm}")
        return redirect(url_for('auth.signup'))

    user = UserModel.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for('auth.signup'))

    new_user = UserModel(
        email=email,
        password=generate_password_hash(password, method='sha256')
    )

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=True)

    return redirect(url_for('main.dashboard'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
