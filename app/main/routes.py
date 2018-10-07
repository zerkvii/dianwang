# coding=utf-8
from flask import render_template, request,redirect,url_for,flash
from flask_login import login_required, current_user
from app.models import User
from app import bcrypt, db
from .forms import UpdateAccountForm
from . import main


@main.route('/user_manage', methods=['GET', 'POST'])
@login_required
def user_manage():
    return render_template('backend/user_manage.html')


@main.route('/record_info', methods=['GET', 'POST'])
@login_required
def record_info():
    return render_template('backend/record_info.html')


@main.route('/add_info', methods=['GET', 'POST'])
@login_required
def add_info():
    return render_template('backend/add_info.html')


@main.route('/user_settings', methods=['GET', 'POST'])
@login_required
def user_settings():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.corpname=form.corpname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash(u'修改已完成', 'alert')
        return redirect(url_for('main.user_manage'))
    return render_template('backend/user_settings.html', form=form)
