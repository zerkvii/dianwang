import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'zee.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'ZERKVII'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'uchbkqerldjeecig'


if __name__ == '__main__':
    print(basedir)
