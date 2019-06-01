import requests
import os

API_URL = 'http://127.0.0.1:5000/apis'
API_KEY = ''

if __name__ == '__main__':
    # response = requests.get('{}/files'.format(API_URL))
    file_dir = os.path.join(os.getcwd(), 'demo')
    filename = 'gz20190126'
    json_file = filename + '.json'
    rar_file = filename + '.rar'
    md5_file = filename + '.md5'
    payload = {"param_1": "value_1", "param_2": "value_2"}
    files = {json_file: open(os.path.join(file_dir, json_file), 'rb'),
             md5_file: open(os.path.join(file_dir, md5_file), 'rb'),
             rar_file: open(os.path.join(file_dir, rar_file), 'rb')
             }

    response = requests.post(API_URL + '/files/all/gz2019012', files=files)
    print(response.json)
    # response = requests.post(
    #     '{}/files'.format(API_URL),, data = content
    # )
    # print(response.json())
