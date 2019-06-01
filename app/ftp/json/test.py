import json

from app.repository import *

if __name__ == '__main__':
    file = open('test.json', encoding='utf8')
    f = json.load(file)
    for x in range(10):
        record_dict = f['record']
        record_dict['serial_number'] = 'gz201904027' + str(x)
        print(record_dict)
        record = Record.from_json(json.dumps(record_dict))
        record.save()
