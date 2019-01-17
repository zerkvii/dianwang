from flask import jsonify, render_template

from . import api


@api.route('/records/', methods=['GET'])
def get_records():
    records = {
        'no.1': {
            'id': 1,
            'info': 'info'},
        'no.2': {
            'id': 2,
            'info': 'info'
        }
    }
    return jsonify(records)


@api.route('/records/<int:id>')
def get_record(id):
    record = {
        'id': id,
        'info': 'info'
    }
    return jsonify(record)
