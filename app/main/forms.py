# coding=utf-8
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError, EqualTo

from app import bcrypt
from app.models import User


# from flask_pagedown.fields import PageDownField


class UpdateAccountForm(FlaskForm):
    corpname = StringField(u'公司名称', validators=[DataRequired(message=u'输入不为空')])
    username = StringField(u'用户名', validators=[DataRequired(message=u'输入不为空'), Length(min=2, max=22, message='长度2-22')])
    email = StringField(u'邮箱', validators=[DataRequired(message=u'输入不为空'), Email(message=u'邮箱格式不合法')])
    image = FileField(u'上传照片 ', validators=[FileAllowed(['jpg', 'png'], message=u'请选择jpg或者png格式文件')])
    contact_number = StringField(u'联系电话',
                                 validators=[DataRequired(message=u'输入不为空')])
    address = StringField(u'地址', validators=[DataRequired(message=u'输入不为空')])
    official_web = StringField(u'官网', validators=[DataRequired(message=u'输入不为空')])
    password = PasswordField(
        validators=[DataRequired(message=u'输入不为空'),
                    Regexp('^[a-zA-Z][a-zA-Z0-9]+$', message=u'密码必须包含字母'),
                    Length(6, 20, message=u'长度为6-20')])
    # new_password = PasswordField(
    #     validators=[DataRequired(message=u'输入不为空'),
    #                 Regexp('^[a-zA-Z][a-zA-Z0-9]+$', message=u'密码必须包含字母'),
    #                 Length(6, 20, message=u'长度为6-20')])
    # confirm_password = PasswordField(
    #     validators=[DataRequired(message=u'输入不为空'), EqualTo('new_password', message=u'两次输入不一致')])
    new_password = PasswordField()
    confirm_password = PasswordField(validators=[EqualTo('new_password', message=u'两次输入不一致')])

    def validate_corpname(self, corpname):
        if corpname.data != current_user.corpname:
            user = User.query.filter_by(corpname=corpname.data).first()
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

    def validate_password(self, password):
        if bcrypt.check_password_hash(current_user.password, password.data):
            pass
        else:
            raise ValidationError(u'密码错误')

    def validate_new_password(self, new_password):
        if new_password.data.strip() != '':
            if len(new_password.data) <= 6:
                raise ValidationError(u'新密码长度应大于6位')

    submit = SubmitField()


class RecordForm(FlaskForm):
    corpname = StringField(u'公司名称', validators=[DataRequired(message=u'输入不为空')])
    agent = StringField(u'申报人姓名', validators=[DataRequired(message=u'输入不为空')])
    record_title = StringField(u'备案标题', validators=[DataRequired(message=u'输入不为空')])
    record_type = SelectField(u'备案类型', choices=[u'第一类', u'第二类'])
    record_batch_time = DateField(u'生产时间', format='%Y-%m-%d', validators=[DataRequired(message=u'请输入批次')])
    record_batch_serial = SelectField(u'生产批次', choices=[u'第一批', u'第二批', u'第三批'])
    record_file_name = StringField(u'文件名', validators=[DataRequired(message=u'输入文件名')])


class TestForm(FlaskForm):
    picture = FileField(u'上传照片 ', validators=[FileAllowed(['jpg', 'png'], message=u'请选择jpg或者png格式文件')])
    submit = SubmitField()
