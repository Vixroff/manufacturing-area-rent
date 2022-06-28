from webapp import db

"""
Модели таблиц базы данных. 
Связи в таблицах: "buildings" one-to-many "sections", "tenants" one-to-many "sections" 
"""

class Buildings(db.Model):
    __tablename__ = 'buildings'
    id = db.Column(db.Integer, primary_key = True)
    street = db.Column(db.String)
    index = db.Column(db.String, unique = True)
    function = db.Column(db.String) 
    count_floors = db.Column(db.Integer)
    sections = db.relationship('Sections', back_populates = 'building')
    photo = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return f"{self.street}, {self.index}"


class Tenants(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    email = db.Column(db.String)
    personal_phone = db.Column(db.String) 
    commercial_phone = db.Column(db.String)
    start_rent = db.Column(db.Date)
    end_rent = db.Column(db.Date)
    section = db.relationship('Sections', back_populates ='tenant')

    def __repr__(self):
        return f"{self.name}"


class Sections(db.Model):
     __tablename__ = 'sections'
     id = db.Column(db.Integer, primary_key = True)
     building_id = db.Column(db.String, db.ForeignKey('buildings.id'))
     index = db.Column(db.Integer)
     floor = db.Column(db.Integer)
     function = db.Column(db.String)
     area = db.Column(db.Float)
     tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
     tenant = db.relationship('Tenants', back_populates = 'section')
     building = db.relationship('Buildings', back_populates = 'sections')
     
     def __repl__(self):
        return f"{self.index}"

