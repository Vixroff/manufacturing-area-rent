import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DataBase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YANDEX_API_KEY_MAP = '4e365bd6-9813-4000-95f3-a859675b0dcc'