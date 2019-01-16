# coding=utf-8
from flask import render_template, request
from flask_login import login_required
from flask_socketio import emit

from . import main
from .. import socketio


@socketio.on('event')
def test_message():
    emit('my response', {'data': 'info'})


@main.route('/backend', methods=['GET', 'POST'])
@login_required
def backend():
    # socketio.emit('message', {'data': 'T'}, namespace='/backend')
    return render_template('backend.html', title=u'系统信息')


# 备案概览
@main.route('/backend/overview', methods=['GET', 'POST'])
@login_required
def overview():
    return render_template('backend_overview.html', title=u'备案概览')


# 查看备案
@main.route('/backend/lookup', methods=['GET', 'POST'])
@login_required
def lookup():
    # records = Record.query.all()
    # send recorrds to specified
    return render_template('backend_lookup.html', title=u'查看备案')


#  审批备案
@main.route('/backend/approval', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        record_data = request.get_json()
        return render_template('split_backend/backend_lookup.html')
    return render_template('backend_approval.html', title=u'审批备案')


# 修改备案
@main.route('/backend/help', methods=['GET', 'POST'])
@login_required
def modify():
    if request.method == 'POST':
        modify_data = request.get_json()
        return
    return render_template('backend_help.html', title=u'帮助')


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
