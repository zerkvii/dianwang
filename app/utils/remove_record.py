import os

up_dir = os.path.dirname
UPLOAD_DIRECTORY = os.path.join(os.getcwd(), 'api_uploaded_files')


def remove_record(id: str):
    '''

    :param id:
    :return:
    '''
    removed_files = [id + '.json', id + '.md5', id + '.zip']

    for (json_file, md5_file, zip_file) in zip(os.listdir(os.path.join(UPLOAD_DIRECTORY, 'json')), os.listdir(
            os.path.join(UPLOAD_DIRECTORY, 'md5')), os.listdir(os.path.join(UPLOAD_DIRECTORY, 'zip'))):
        if json_file in removed_files:
            os.remove(os.path.join(UPLOAD_DIRECTORY, 'json', json_file))
        if md5_file in removed_files:
            os.remove(os.path.join(UPLOAD_DIRECTORY, 'md5', md5_file))
        if zip_file in removed_files:
            os.remove(os.path.join(UPLOAD_DIRECTORY, 'zip', zip_file))


if __name__ == '__main__':
    remove_record('gz20190226')
