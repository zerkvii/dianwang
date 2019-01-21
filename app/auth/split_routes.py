# -*- coding=utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify, flash
from flask_login import logout_user, login_user, current_user

from app import bcrypt, db
from app.models import User
from . import auth


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash(u'已经登陆', category='warning')
        return redirect(url_for('main.backend'))
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
            info = {'information': u'成功注册', 'next_page': 'login'}
            flash(u'注册成功，现在可以登录', 'success')
            return jsonify(info), 200
            # return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=u'备案系统注册')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(u'已经登陆', category='info')
        return redirect(url_for('main.backend'))
    if request.method == 'POST':
        next_page = request.args.get(u'next')
        login_data = request.get_json()
        username = login_data['username']
        password = login_data['password']
        user = User.query.filter_by(username=username).first() or User.query.filter_by(email=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            info = {}
            if next_page:
                info['next_page'] = '{}'.format(next_page)
                flash(u'{} 登录成功'.format(user.username), 'success')
                return jsonify(info), 200
            else:
                info['next_page'] = 'backend'
                flash(u'{} 登录成功'.format(user.username), 'success')
                return jsonify(info), 200
        else:
            info = {
                'information': '用户名或密码错误'
            }
            return jsonify(info), 400
        # flash(u'注册成功，现在可以登录', 'success')
    return render_template('auth/login.html', title=u'备案系统登录')


@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    pass
    # return render_template('forgot.html', title=u'忘记密码')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# @login_manager.user_loader
# def load_user(user_id):
#     return None
