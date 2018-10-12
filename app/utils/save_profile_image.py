import os
import secrets
from flask import current_app
from PIL import Image


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = current_app.root_path+'/static/auth/images/user/'+picture_fn
    print(picture_path)
    output_size = (180, 180)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
