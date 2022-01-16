from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField, SelectField, EmailField, PasswordField, validators


class MainForm(FlaskForm):
    choices = [(30, '30 minutes'), (60, '1 hour'), (360, '6 hours'), (1440, '1 day'), (10080, '1 week')]

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
    passwordConfirm = PasswordField(name='passwordConfirm', label='Confirm Password:', validators=[validators.length(min=6, max=18)])
    submit = SubmitField('Signup')
