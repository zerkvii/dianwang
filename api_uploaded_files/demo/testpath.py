import json
import os

if __name__ == '__main__':
    filepath = os.path.join(os.getcwd(), 'gz20190125.json')
    jf = open(filepath, 'r', encoding='utf-8')
    cont = json.load(jf)
    print(cont)
