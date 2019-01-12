import os
import pymysql

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'zee.sqlite')
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:12345678@localhost/state_grid'
    # POSTGRES = {
    #     'user': 'postgres',
    #     'pwd': '12345678',
    #     'db': 'state_grid',
    #     'host': 'localhost',
    #     'port': '5432',
    # }
    # SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pwd)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'ZERKVII'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'uchbkqerldjeecig'
    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = "6Ldiq2gUAAAAANfr7yU1ygZoAYUkkY-CWMcWotEv"
    RECAPTCHA_SECRET_KEY = "6Ldiq2gUAAAAAA9c_eAsYHPqrgiSD8tDVAz2swOM"
    # RECAPTCHA_THEME = "dark"
    RECAPTCHA_TYPE = 'image'
    ENV = "DEBUG"
    DEBUG = True
    JSON_AS_ASCII = False
    # RECAPTCHA_SIZE = "compact"
    # RECAPTCHA_RTABINDEX = 10
