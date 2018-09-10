from . import db
from datetime import datetime
from flask_login import UserMixin


class Permission:
    READ=0x01
    MODIFY=0x02


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(40), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)


# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.String(64), nullable=False, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     content = db.Column(db.String(128), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     category = db.Column(db.Integer, nullable=False, default=0)
#     keyword = db.Column(db.String(64), nullable=True)
#     post_type = db.Column(db.Integer, nullable=False)


class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
