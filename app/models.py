import os

from flask_login import UserMixin

from . import db, login_manager
from .utils.date_util import get_current_time


class Permission:
    READ = 0x01
    MODIFY = 0x02


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # 厂商名
    corpname = db.Column(db.String(30), unique=True, nullable=False)
    # 用户名
    username = db.Column(db.String(30), unique=True, nullable=False)
    # 邮件
    email = db.Column(db.String(120), unique=True, nullable=False)
    # 厂商地址
    address = db.Column(db.String(120), default='未更改')
    # 官网地址
    official_web = db.Column(db.String(128), default='https://www.official.com')
    # 联系电话
    contact_number = db.Column(db.String(36), default='0000-0000000')
    # logo
    image = db.Column(db.String(128), nullable=False, default='default.png')
    # 密码
    password = db.Column(db.String(128), nullable=False)
    # 厂商序列号
    manufacturer_number = db.Column(db.String(4))
    # 注册时间
    register_time = db.Column(db.String(40), default=get_current_time)
    # posted_records = db.relationship('Record', backref='record_applicant', lazy=True)


class Staff(db.Model):
    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True)
    # 员工序列号
    staff_number = db.Column(db.String(20), nullable=False)
    # 密码
    staff_password = db.Column(db.String(128), nullable=False)
    # 类型 0 省网 1 国网
    staff_type = db.Column(db.Integer, nullable=False, default=0)
    # 注册时间
    register_time = db.Column(db.String(40), default=get_current_time)

    # examined_records = db.relationship('Record', backref='record_checker', lazy=True)


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)

    # 备案序列号
    record_serial_number = db.Column(db.String(16), nullable=False, default='AAAAAAAAAAAAAAAA')

    # 备案类型,带系统/不带系统
    record_type = db.Column(db.Boolean, nullable=False, default=False)

    # 备案申请日期
    record_post_date = db.Column(db.String(64), nullable=False, default=get_current_time)

    # 备案软件版本号
    record_software_version = db.Column(db.String(16), nullable=False)

    # 备案软件送检顺序
    record_order = db.Column(db.Integer, nullable=False)

    # 备案厂商
    record_manufacturer = db.Column(db.String(4), nullable=False)

    # 备案审批状态
    record_state = db.Column(db.Integer, nullable=False, default=0)

    # 备案文件路径
    record_file_uri = db.Column(db.String(128), nullable=False, default=os.getcwd() + os.sep + 'files')

    # 备案文件名（文件夹）
    record_file_name = db.Column(db.String(64), default='None')

    # 备案审批人
    record_inspector = db.Column(db.String(32), nullable=False)

    record_test = db.Column(db.Integer, default=0)


# manufacturer = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
# librarian = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)
# submit_date = db.Column(db.String(64), nullable=False, default=get_current_time)
# approval_date = db.Column(db.String(64), nullable=True)
# record_state = db.Column(db.Integer, nullable=False, default=0)
# valid_date = db.Column(db.String(64), nullable=False)
# record_title = db.Column(db.Text, nullable=False)
# serial_number = db.Column(db.Integer, nullable=False, default=generate_serial_number)
# record_description = db.Column(db.Text, nullable=False)
# production_batch = db.Column(db.Integer, nullable=False)
# production_type = db.Column(db.Integer, nullable=False, default=0)
# production_url = db.Column(db.String(128), nullable=False)
# edited_time = db.Column(db.Integer, nullable=False, default=0)


class Test_field(db.Model):
    __tablename__='test'
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.TEXT)