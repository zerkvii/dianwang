# -*- coding: utf-8 -*-
from flask import render_template, url_for, flash, redirect, request, session, abort
from flask_login import login_user, current_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from app import bcrypt, db
from app.models import User
from . import auth
from app import recaptcha


@auth.route('/')
def index():
    return render_template('index.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
    #     db.session.add(user)
    #     db.session.commit()
    #     return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        print form.username.data
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         if next_page:
    #             return redirect(next_page)
    #         else:
    #             return redirect(url_for('main.home'))
    #     else:
    #         flash('登录失败，请检查账号或者密码', 'danger')

    return render_template('auth/login.html', title='login', form=form)


@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('auth/forgot.html', title='forgot')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
