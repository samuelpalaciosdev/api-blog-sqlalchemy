from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import ForeignKey
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # articles = db.relationship('Article', backref='user')

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
        }

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    date_posted = db.Column(db.DateTime(), default=datetime.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')

    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'date_posted': self.date_posted,
            'user': self.user.username
        }
