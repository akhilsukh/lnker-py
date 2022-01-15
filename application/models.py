from app import db
from sqlalchemy import Column, DateTime, String
from flask_login import UserMixin


class LinkModel(db.Model):
    __tablename__ = 'links'

    code = Column(String(), primary_key=True)
    link = Column(String())
    date = Column(DateTime())

    def __init__(self, code, link, date):
        self.code = code
        self.link = link
        self.date = date

    def __repr__(self):
        return f"{self.code}:{self.link[:10] + ('...' if len(self.link) > 10 else '')}, created on {self.date}"


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    uid = Column(String(), primary_key=True)
    email = Column(String())
    password = Column(String())

    def __init__(self, uid, email, password):
        self.uid = uid
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.email}"


class VisitModel(db.Model):
    __tablename__ = 'visits'

    code = Column(String())
    date = Column(String(), primary_key=True)

    def __init__(self, code, date):
        self.code = code
        self.date = date

    def __repr__(self):
        return f"{self.code}:{self.date}"
