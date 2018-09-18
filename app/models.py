from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from .utils.date_util import get_current_time


class Permission:
    READ = 0x01
    MODIFY = 0x02


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    # file_number = db.Column(db.String(20), nullable=False)
    # file_type = db.Column(db.Integer, nullable=False, default=0)
    # file_approval_status = db.Column(db.Integer, nullable=False, default=0)
    # file_submit_date = db.Column(db.String(64), nullable=False, default=get_current_time)
    # file_title = db.Column(db.String(64), nullable=False)
    # file_content = db.Column(db.Text)
    # file_checked_date = db.Column(db.String(64), nullable=True)
    # file_location = db.Column(db.String(128), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)
    # user_files = db.relationship('File', foreign_keys=['user_id'], backref='files', lazy=True)
    # staff_files = db.relationship('File', foreign_keys=['staff_id'], backref='files', lazy=True)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # corpname = db.Column(db.String(30), unique=True, nullable=False)
    # username = db.Column(db.String(30), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    # image = db.Column(db.String(40), nullable=False, default='default.png')
    # password = db.Column(db.String(128), nullable=False)
    post_files = db.relationship('File', backref='file_applicant', lazy=True)

    # posts = db.relationship('Post', backref='author', lazy=True)


class Staff(db.Model):
    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True)
    # staff_number = db.Column(db.String(20), nullable=False)
    # staff_password = db.Column(db.String(128), nullable=False)
    # files = db.relationship('File', back_populates='staff', lazy=True)
    check_files = db.relationship('File', backref='file_checker', lazy=True)


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
