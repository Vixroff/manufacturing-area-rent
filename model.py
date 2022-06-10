from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base, engine

"""
Модели таблиц базы данных. 
Связи в таблицах: "buildings" one-to-many "sections", "tenants" one-to-many "sections" 
"""

class Buildings(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key = True)
    street = Column(String)
    index = Column(String, unique = True)
    function = Column(String) 
    count_floors = Column(Integer)
    sections = relationship('Sections', back_populates = 'building')
    photo = Column(String)
       
    def __repr__(self):
        return f"{self.sections}, {self.index}"


class Tenants(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True)
    email = Column(String)
    personal_phone = Column(String) 
    commercial_phone = Column(String)
    start_rent = Column(Date)
    end_rent = Column(Date)
    section = relationship('Sections', back_populates ='tenant')

    def __repr__(self):
        return f"{self.name}"


class Sections(Base):
     __tablename__ = 'sections'
     id = Column(Integer, primary_key = True)
     building_id = Column(String, ForeignKey('buildings.id'))
     index = Column(Integer)
     floor = Column(Integer)
     function = Column(String)
     area = Column(Float)
     tenant_id = Column(Integer, ForeignKey('tenants.id'))

     tenant = relationship('Tenants', back_populates = 'section')
     building = relationship('Buildings', back_populates = 'sections')
     
     def __repl__(self):
        return f"{self.index}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
