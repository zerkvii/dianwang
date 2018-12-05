# coding=utf-8
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.utils.date_util import get_current_time
from app import bcrypt, db
from . import main
from .forms import UpdateAccountForm, RecordForm
from ..utils.save_profile_image import save_picture


@main.route('/user_manage', methods=['GET', 'POST'])
@login_required
def user_manage():
    return render_template('backend/user_manage.html')


# 查看备案
@main.route('/check_info', methods=['GET', 'POST'])
@login_required
def check_info():
    return render_template('backend/check_info.html')


# 增加备案
@main.route('/add_info', methods=['GET', 'POST'])
@login_required
def add_info():
    if request.method == 'GET':
        form = RecordForm()
        form.corpname.data = current_user.corpname
        form.request_date.data = get_current_time()
        form.agent.data = current_user.username
    else:
        form = RecordForm()
    if form.validate_on_submit():
        flash(u'修改已完成', 'alert')
        return redirect(url_for('main.user_manage'))
    return render_template('backend/add_info.html', form=form)


# 修改备案
@main.route('/modify_info', methods=['GET', 'POST'])
@login_required
def modify_info():
    return render_template('backend/modify_info.html')


@main.route('/user_settings', methods=['GET', 'POST'])
@login_required
def user_settings():
    if request.method == 'GET':
        form = UpdateAccountForm()
        form.corpname.data = current_user.corpname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.address.data = current_user.address
        form.contact_number.data = current_user.contact_number
        form.official_web.data = current_user.official_web
    else:
        form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.corpname = form.corpname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.address = form.address.data
        current_user.contact_number = form.contact_number.data
        current_user.official_web = form.official_web.data
        if len(form.new_password.data.strip()) > 0:
            current_user.password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
        if form.image.data:
            current_user.image = save_picture(form.image.data)
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash(u'修改已完成', 'alert')
        return redirect(url_for('main.user_manage'))
    return render_template('backend/user_settings.html', form=form)


@main.route('/user_messages', methods=['GET', 'POST'])
@login_required
def user_messages():
    return render_template('backend/user_messages.html')


# @main.route('/test', methods=['GET', 'POST'])
# @login_required
# def test():
#     form = TestForm()
#     if form.validate_on_submit():
#         print(form.picture.data)
#         return redirect(test)
#     return render_template('backend/test.html', form=form)


@main.route('/user_help', methods=['GET', 'POST'])
@login_required
def user_help():
    return render_template('backend/user_help.html')


@main.route('/files_upload', methods=['POST'])
@login_required
def files_upload():
    pass

