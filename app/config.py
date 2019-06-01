import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = secrets.token_hex(24)
    # REDIS_URL = "redis://localhost"
    # CELERY_BROKER_URL="redis://localhost:6379/0"
    # CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    ENV = "DEBUG"
    # threaded = True
    DEBUG = True
    JSON_AS_ASCII = False
    STATIC_FOLDER = 'templates/auth'
