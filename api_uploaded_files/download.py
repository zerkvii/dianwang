import requests
import os

API_URL = 'http://127.0.0.1:5000/apis'
API_KEY = ''

if __name__ == '__main__':
    req_file = 'gz20190126'
    file_type = 'zip'

    content = {
        'file': req_file,
        'file_type': file_type
    }
    response = requests.post(API_URL + '/files/download', json=content)
    save_file = req_file + '.' + file_type
    with open(save_file, 'wb') as f:
        f.write(response.content)

