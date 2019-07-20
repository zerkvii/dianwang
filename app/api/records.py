from app.repository import *
from . import api
import re
import os
from werkzeug.utils import secure_filename
from flask import request, abort, jsonify, send_from_directory
import json

UPLOAD_DIRECTORY = os.path.join(os.getcwd(), 'api_uploaded_files')


@api.before_app_request
def create_dir():
    json_dir = os.path.join(UPLOAD_DIRECTORY, 'json')
    md5_dir = os.path.join(UPLOAD_DIRECTORY, 'md5')
    zip_dir = os.path.join(UPLOAD_DIRECTORY, 'zip')
    dirs = [json_dir, md5_dir, zip_dir]
    for folder in dirs:
        if not os.path.exists(folder):
            os.makedirs(folder)


def get_dirs_files(dir):
    return os.listdir(os.path.join(UPLOAD_DIRECTORY, 'json')), os.listdir(
        os.path.join(UPLOAD_DIRECTORY, 'md5')), os.listdir(os.path.join(UPLOAD_DIRECTORY, 'zip'))


@api.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    print(os.getcwd())
    print(UPLOAD_DIRECTORY)

    for (json_file, md5_file, zip_file) in zip(os.listdir(os.path.join(UPLOAD_DIRECTORY, 'json')), os.listdir(
            os.path.join(UPLOAD_DIRECTORY, 'md5')), os.listdir(os.path.join(UPLOAD_DIRECTORY, 'zip'))):
        if json_file and md5_file and zip_file:
            files.append([json_file, md5_file, zip_file])
    return jsonify(files)


@api.route("/files/download", methods=['GET', 'POST'])
def get_file():
    """Download a file."""
    filename = request.json['file']
    file_type = request.json['file_type']
    print(filename)
    directory = os.path.join(os.getcwd(), 'api_uploaded_files', file_type)
    print(directory)
    # return '', 200
    return send_from_directory(directory, filename + '.' + file_type, as_attachment=True)


@api.route('/files/all/<string:s_number>', methods=['POST'])
def upload_all(s_number):
    for x in request.files:
        serial_number = re.findall(r'(.*)\.', x)[0]
        if serial_number != s_number:
            info = {
                'information': '序列号与文件不一致'
            }
            return jsonify(info), 400

    for x in request.files:
        file = request.files[x]
        filename = secure_filename(file.filename)
        path = re.findall(r'\.(.*)', x)[0]
        file.save('./api_uploaded_files/' + path + '/' + filename)
    json_file = open('./api_uploaded_files/json/' + s_number + '.json', 'rb')
    f = json.load(json_file)
    try:
        record_dict = f['record']
    except Exception as e:
        print(e)
    if serial_number == record_dict['serial_number']:
        if len(Record.objects(serial_number=serial_number)) < 1:
            record = Record.from_json(json.dumps(record_dict))
            record.save()
        else:
            try:
                record = Record.objects(serial_number=serial_number).first()
                record.from_json(json.dumps(record_dict))
                print(record.to_json())
                record.save()
            except Exception as e:
                print(e)
    info = {
        'information': '上传成功'
    }
    print(f)
    return jsonify(info), 200


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
