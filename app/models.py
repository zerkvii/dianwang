from . import db, login_manager
from flask_login import UserMixin
from .utils.date_util import get_current_time
from .utils.generate_serial_number import generate_serial_number


class Permission:
    READ = 0x01
    MODIFY = 0x02


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    corpname = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(40), nullable=False, default='default.png')
    password = db.Column(db.String(128), nullable=False)
    posted_records = db.relationship('Record', backref='file_applicant', lazy=True)


class Staff(db.Model):
    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True)
    staff_number = db.Column(db.String(20), nullable=False)
    staff_password = db.Column(db.String(128), nullable=False)
    # files = db.relationship('File', back_populates='staff', lazy=True)
    examined_records = db.relationship('File', backref='file_checker', lazy=True)


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    librarian = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)
    submit_date = db.Column(db.String(64), nullable=False, default=get_current_time)
    approval_date = db.Column(db.String(64), nullable=True)
    record_state = db.Column(db.Integer, nullable=False, default=0)
    valid_date = db.Column(db.String(64), nullable=False)
    record_title = db.Column(db.Text, nullable=False)
    serial_number = db.Column(db.Integer, nullable=False, default=generate_serial_number)
    record_description = db.Column(db.Text, nullable=False)
    production_batch = db.Column(db.Integer, nullable=False)
    production_type = db.Column(db.Integer, nullable=False, default=0)
    production_url = db.Column(db.String(128), nullable=False)
    edited_time = db.Column(db.Integer, nullable=False, default=0)


class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=get_current_time)
