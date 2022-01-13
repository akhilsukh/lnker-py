from app import db
from sqlalchemy import Column, Integer, String, ForeignKey


class LinkModel(db.Model):
    __tablename__ = 'links'

    code = Column(String(), ForeignKey("links.code"), primary_key=True)
    link = Column(String(), ForeignKey("links.link"))
    visits = Column(Integer(), ForeignKey("links.visits"))

    def __init__(self, code, link, visits):
        self.code = code
        self.link = link
        self.visits = visits

    def __repr__(self):
        return f"{self.code}:{self.link}"
