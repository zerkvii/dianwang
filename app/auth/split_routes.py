# -*- coding=utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify
from flask_login import logout_user

from app import bcrypt, db
from app.models import User
from . import auth


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_data = request.get_json()
        username = register_data['username']
        email = register_data['email']
        password = register_data['password']
        toggle = register_data['toggle']
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
        if user:
            info = {
                'information': '用户名或邮件已经存在'
            }
            return jsonify(info), 400
        else:
            user = User(username=username, email=email, password=hashed_pwd, toggle=toggle)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        # flash(u'注册成功，现在可以登录', 'success')
    return render_template('split_auth/register.html', title=u'注册页面')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_data = request.get_json()
        username = login_data['username']
        password = login_data['password']
        user = User.query.filter_by(username=username).first() or User.query.filter_by(email=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return redirect(url_for('main.user_manage'))
        else:
            info = {
                'information': '用户名或密码错误'
            }
            return jsonify(info), 400
        # flash(u'注册成功，现在可以登录', 'success')
    return render_template('split_auth/login.html', title=u'登录页面')


@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('auth/forgot.html', title='forgot')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# @login_manager.user_loader
# def load_user(user_id):
#     return None
