from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import Form, URLField, StringField, SubmitField, validators


class MainForm(FlaskForm):
    code = StringField(name='code', label='Code:', validators=[validators.length(min=2, max=15)])
    link = URLField(name='link', label='Link:', validators=[validators.length(min=5, max=200)])
    submit = SubmitField('Create LNK')


# class redirectClass(FlaskForm):
#     def __init__(self, code, link):
#         self.code = code
#         self.link = link
#
# def register(request):
#     form = redirectForm(request.POST)
#     if form.validate():
#         red = redirectClass(form.code.data, form.link.data)
#         red.save()
#         redirect('404')
#
