import os
from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DataBase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YANDEX_API_KEY_MAP = os.environ.get('YANDEX_API_KEY_MAP')
    TGBOT_TOKEN = os.environ.get('TGBOT_TOKEN')
    TGBOT_CHAT_ID =  os.environ.get('TGBOT_CHAT_ID')