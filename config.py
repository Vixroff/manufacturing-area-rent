import os


basedir = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DataBase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False