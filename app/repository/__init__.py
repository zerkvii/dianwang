"""
mongoengine model
"""

from flask_login import UserMixin
from mongoengine import *

from app import login_manager
from .tools import current_time

connect('sg')


class User(Document, UserMixin):
    email = StringField(required=True)
    username = StringField(max_length=50, unique=True)
    password = StringField()
    register_date = DateTimeField(default=current_time)
    user_type = IntField(default=0)
    avatar = StringField(default='admin.png')

    def get_avatar(self):
        return '/static/admin/avatars/' + self.avatar

    def to_dict(self):
        return dict(self.to_mongo())


class Record(Document):
    serial_number = StringField(unique=True)
    status_flag = BooleanField(default=False)
    back_date = DateTimeField(default=current_time)
    backup_version = StringField()
    producer_name = StringField()
    producer_id = StringField()
    contact_person = StringField()
    contact_number = StringField()
    dianbiao_version = StringField()
    code_version = StringField()
    backup_type = IntField(default=0)
    details = DictField()

    def to_strftime(self):
        return self.back_date.strftime("%Y-%m-%d %H:%M:%S")

    def get_back_type(self):
        if self.backup_type:
            return '不带系统'
        else:
            return '带系统'

    def get_details(self):
        return dict(self.details)


class FileUser(Document):
    username = StringField(unique=True)
    password = StringField()


@login_manager.user_loader
def load_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return None
    return user
