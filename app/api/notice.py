from flask import request, jsonify

from app.repository import *
from . import api

global NOTICE_LIST, FLAG
NOTICE_LIST = set()


@api.route('/notice', methods=['GET', 'POST'])
def notice():
    global NOTICE_LIST
    data = None
    if request.method == 'POST':
        new_records = set(Record.objects(status_flag=False))
        added_flag = new_records - NOTICE_LIST
        NOTICE_LIST = new_records
        first_flag = request.form['first']
        if request.form['type'] == '0' and len(added_flag) > 0:
            data = {'urls': [x.serial_number for x in added_flag], 'date': [x.to_strftime() for x in added_flag]}
        if first_flag == '0':
            data = {'urls': [x.serial_number for x in NOTICE_LIST], 'date': [x.to_strftime() for x in NOTICE_LIST]}

    return jsonify(data), 200
