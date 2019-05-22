from app.repository import *
from . import api
import re
import os
from werkzeug.utils import secure_filename
from flask import request, abort, jsonify, send_from_directory

UPLOAD_DIRECTORY = os.path.join(os.getcwd(), 'api_uploaded_files')

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@api.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    print(os.getcwd())
    print(UPLOAD_DIRECTORY)

    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@api.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@api.route('/files/all', methods=['POST'])
def upload_all():
    filename = ''
    for x in request.files:
        serial_number = re.findall(r'.*\.', x)[0]
        path = re.findall(r'\.(.*)', x)[0]
        print(path)
        file = request.files[x]
        filename = secure_filename(file.filename)
        print(filename)
        file.save('./api_uploaded_files/' + path + '/' + filename)
    return "", 200


# @api.route("/files/<filename>", methods=["POST"])
# def post_file(filename):
#     """Upload a file."""
#
#     if "/" in filename:
#         # Return 400 BAD REQUEST
#         abort(400, "no subdirectories directories allowed")
#
#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(request.data)
#
#     # Return 201 CREATED
#     return "", 201


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
