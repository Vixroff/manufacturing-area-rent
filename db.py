import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

"""
Здесь команды взаимодействия с баззой данных.
Все, как в лекциях Миши.
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conn = 'sqlite:///' + os.path.join(BASE_DIR, 'DataBase.db')

engine = create_engine(conn)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
