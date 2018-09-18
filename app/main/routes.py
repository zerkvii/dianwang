from flask import render_template, request
from flask_login import login_required
from app.models import  User
from . import main


@main.route('/user_manage', methods=['GET', 'POST'])
@login_required
def user_manage():
    return render_template('backend/user_manage.html')


@main.route('/record_info', methods=['GET', 'POST'])
def record_info():
    return render_template('backend/record_info.html')


@main.route('/add_info', methods=['GET', 'POST'])
def add_info():
    return render_template('backend/add_info.html')
