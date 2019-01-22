from flask import jsonify, render_template, request
from app.models import Record
from . import api
# from app import socketio
#
#
# @socketio.on('connect', namespace='upload')
# def on_connect():
#     print('info')


@api.route('/records/post', methods=['POST'])
def post_record():
    json_data = request.get_json()
    # print(json_data)
    serial_number = json_data['serial']
    record = Record.query.filter_by(serial_number=serial_number).first()
    if not record:
        data = {
            "information": "not exist"
        }
        return jsonify(data), 404
    else:
        data = {
            "information": "exist"
        }
        return jsonify(data), 200

#
# @api.route('/records/', methods=['GET'])
# def get_records():
#     records = {
#         'no.1': {
#             'id': 1,
#             'info': 'info'},
#         'no.2': {
#             'id': 2,
#             'info': 'info'
#         }
#     }
#     return jsonify(records)
#
#
# @api.route('/records/<int:id>')
# def get_record(id):
#     record = {
#         'id': id,
#         'info': 'info'
#     }
#     return jsonify(record)
