from flask import Blueprint

auth = Blueprint('auth', __name__)

# from . import routes
# below is split route
from . import split_routes