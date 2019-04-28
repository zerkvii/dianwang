from flask import request, jsonify

from app.repository import *
from . import api

# thread = None
# thread_lock = Lock()


# async def notice():
global NOTICE_LIST, FLAG
NOTICE_LIST = []
FLAG = False


@api.route('/notice', methods=['GET', 'POST'])
def notice():
    global NOTICE_LIST, FLAG
    data = None
    print(NOTICE_LIST)
    if request.method == 'POST':
        new_records = Record.objects(status_flag=False)
        if request.form['type'] == '0' and new_records.count() > 0:
            url_list = [x for x in new_records if x not in NOTICE_LIST]
            print(url_list, len(NOTICE_LIST))
            NOTICE_LIST.append(url_list)
            data = {'urls': [x.serial_number for x in url_list]}
    return jsonify(data), 200
