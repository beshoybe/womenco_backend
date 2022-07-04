

from app import db
class Area(db.Model):
    __tablename__ = "area"
    id  = db.Column(db.Integer,primary_key= True)
    governerate = db.Column(db.String(20))
    city = db.Column(db.String(20),unique=True)
    arabicgovernerate = db.Column(db.String(20))
    arabiccity = db.Column(db.String(20))

    def create(self):
        db.session.add(self)
        db.session.commit()
    def __init__(self,data):
        self.governerate = data['governerate']
        self.city = data['city']
        self.arabicgovernerate = data['arabicgovernerate']
        self.arabiccity = data['arabiccity']
    def delete(self):
        db.session.delete(self)
        db.session.commit()       
class VendorArea(db.Model):
    __tablename__ = "vendorarea"
    id  = db.Column(db.Integer,primary_key= True)
    governerate = db.Column(db.String(20))
    arabicgovernerate = db.Column(db.String(20))
    city = db.Column(db.String(20))
    arabiccity = db.Column(db.String(20))
    added_by = db.Column(db.Integer,db.ForeignKey('vendor.id'))
    def create(self):
        db.session.add(self)
        db.session.commit()
    def __init__(self,data):
        self.governerate = data['governerate']
        self.city = data['city']
        self.arabicgovernerate = data['arabicgovernerate']
        self.arabiccity = data['arabiccity']
    def delete(self):
        db.session.delete(self)
        db.session.commit()  