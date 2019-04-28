# coding=utf-8
from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required
from . import main
from app.repository import *


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
    records = Record.objects(status_flag=True).all()
    # send recorrds to specified
    return render_template('backend_lookup.html', title=u'查看备案', records=records)


#  审批备案
@main.route('/backend/approval', methods=['GET', 'POST'])
@login_required
def approval():
    # print('ok')
    records = Record.objects(status_flag=False).all()
    if request.method == 'POST':
        record_data = request.get_json()
        if record_data['action'] == 1:
            data = {
                "next_page": "lookup"
            }
            record = Record.query.filter_by(serial_number=record_data['serial_number']).first()
            record.status_flag = True
            record.save()
            flash('审批成功')
            return jsonify(data), 200
        else:
            data = {
                "next_page": "error_record"
            }
            flash('错误反馈')
            return jsonify(data), 200
    return render_template('backend_approval.html', title=u'审批备案', records=records)


# 帮助
@main.route('/backend/help', methods=['GET', 'POST'])
@login_required
def help():
    # if request.method == 'POST':
    #     modify_data = request.get_json()
    #     return
    return render_template('backend_help.html', title=u'帮助')


# 查看指定备案
@main.route('/backend/records/<string:str>', methods=['GET'])
def record_detail(str):
    title = '备案号 ' + str
    record = Record.objects(serial_number=str).first()
    if record:
        return render_template('backend_detail.html', record=record, title=title)


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
