from flask_wtf import FlaskForm
from wtforms import Form, URLField, StringField, SubmitField, SelectField, validators


class MainForm(FlaskForm):
    choices = [(30, '30 minutes'), (60, '1 hour'), (360, '6 hours'), (1440, '1 day'), (10080, '1 week')]

    code = StringField(name='code', label='Code:', validators=[validators.length(min=2, max=15)])
    link = URLField(name='link', label='Link:', validators=[validators.length(min=5, max=200)])
    expire = SelectField(name='expire', label='Expiry:', choices=choices)
    submit = SubmitField('Create LNK')
