# coding=utf-8
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from app.models import User


class UpdateAccountForm(FlaskForm):
    corpname = StringField(u'公司名称', validators=[DataRequired(message=u'输入不为空')])
    username = StringField(u'用户名', validators=[DataRequired(message=u'输入不为空'), Length(min=2, max=22, message='长度2-22')])
    email = StringField(u'邮箱', validators=[DataRequired(message=u'输入不为空'), Email(message=u'邮箱格式不合法')])
    picture = FileField(u'上传照片 ', validators=[FileAllowed(['jpg', 'png'], message=u'请选择jpg或者png格式文件')])
    password = PasswordField(
        validators=[DataRequired(message=u'输入不为空'),
                    Regexp('^[a-zA-Z][a-zA-Z0-9]+$', message=u'密码必须包含字母'),
                    Length(6, 20, message=u'长度为6-20')])
    confirm_password = PasswordField(
        validators=[DataRequired(message=u'输入不为空'), EqualTo('password', message=u'两次输入不一致')])

    def validate_corpname(self, corpname):
        if corpname.data != current_user.corpname:
            user = User.query.filter_by(username=corpname.data).first()
            if user:
                raise ValidationError(u'此公司已经注册')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(u'此用户名已存在')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(u'此邮箱已存在')

    submit = SubmitField()
