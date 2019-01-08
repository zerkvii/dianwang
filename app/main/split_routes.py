# coding=utf-8
from flask import render_template, request
from flask_login import login_required

from . import main


@main.route('/backend', methods=['GET', 'POST'])
@login_required
def backend():
    return render_template('split_backend/backend.html', title=u'后台')


# 查看备案
@main.route('/backend/lookup', methods=['GET', 'POST'])
@login_required
def lookup():
    # records = Record.query.all()
    # send recorrds to specified
    return render_template('split_backend/backend_lookup.html')


# 增加备案
@main.route('/backend/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        record_data = request.get_json()
        return render_template('split_backend/backend_lookup.html')
    return render_template('split_backend/backend_add.html')


# 修改备案
@main.route('/backend/modify', methods=['GET', 'POST'])
@login_required
def modify():
    if request.method == 'POST':
        modify_data = request.get_json()
        return
    return render_template('split_backend/backend_modify.html')


@main.route('/backend/chinfo', methods=['GET', 'POST'])
@login_required
def chinfo():
    return render_template('split_backend/backend_chinfo.html')


@main.route('/backend/dash', methods=['GET', 'POST'])
@login_required
def dash():
    return render_template('split_backend/backend_dash.html')


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
