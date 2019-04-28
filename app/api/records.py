from flask import jsonify, request, g

from app.repository import *
from . import api




@api.route('/records/post', methods=['POST'])
def post_record():
    json_data = request.get_json()
    serial_number = json_data['serial']
    record = Record.objects(serial_number=serial_number).first()
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
