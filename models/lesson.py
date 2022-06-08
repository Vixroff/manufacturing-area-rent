from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base

association_table = Table('association', Base.metadata,
                          Column('lesson_id', Integer, ForeignKey('lessons.id')),
                          Column('group_id', Integer, ForeignKey('groups.id'))
                          )


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_title = Column(String)
    groups = relationship('Group', secondary=association_table, backref='group_lesson')
