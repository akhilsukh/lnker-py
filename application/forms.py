from calendar import week

from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField, SelectField, EmailField, PasswordField, validators
from flask_login import current_user
from datetime import datetime, timedelta


class MainForm(FlaskForm):
    choices = [(timedelta(minutes=15), '15 minutes'), (timedelta(hours=1), '1 hour'),
               (timedelta(hours=6), '6 hours'), (timedelta(days=1), '1 day'),
               (timedelta(weeks=1), '1 week')]

    if current_user and current_user.is_authenticated():
        choices.append((timedelta.max, 'Permanent'))

    code = StringField(name='code', label='Code:', validators=[validators.length(min=2, max=15)])
    link = URLField(name='link', label='Link:', validators=[validators.length(min=5, max=200)])
    expire = SelectField(name='expire', label='Expiry:', choices=choices)
    submit = SubmitField('Create LNK')


class LoginForm(FlaskForm):
    email = EmailField(name='email', label='Email:', validators=[])
    password = PasswordField(name='password', label='Password:', validators=[validators.length(min=6, max=18)])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = EmailField(name='email', label='Email:', validators=[])
    password = PasswordField(name='password', label='Password:', validators=[validators.length(min=6, max=18)])
    passwordConfirm = PasswordField(name='passwordConfirm', label='Confirm Password:',
                                    validators=[validators.length(min=6, max=18)])
    submit = SubmitField('Signup')
