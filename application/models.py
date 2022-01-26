from app import db
from sqlalchemy import Column, DateTime, String, Integer
from flask_login import UserMixin


class LinkModel(db.Model):
    __tablename__ = 'links'

    code = Column(String, primary_key=True)
    link = Column(String)
    id = Column(Integer)
    date_created = Column(DateTime)
    date_expiry = Column(DateTime)

    def __init__(self, code, link, date_created, date_expiry, id):
        self.code = code
        self.link = link
        self.date_created = date_created
        self.date_expiry = date_expiry
        self.id = id

    def __repr__(self):
        return f"{self.code}:{self.link[:10] + ('...' if len(self.link) > 10 else '')}, " \
               f"created on {self.date} by {self.id}"


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __init__(self, email, password):
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
