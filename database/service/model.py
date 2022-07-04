
from app import db
class Cleaning(db.Model):
    __tablename__ = "cleaning_service"
    id  = db.Column(db.Integer,db.ForeignKey('vendor.id'),primary_key= True)
    home120 = db.Column(db.String(20))
    home200 = db.Column(db.String(20))
    home250 =db.Column(db.String(20))
    home300 =db.Column(db.String(20))
    home350 =db.Column(db.String(20))
    home400 =db.Column(db.String(20))
    flat120 = db.Column(db.String(20))
    flat200 = db.Column(db.String(20))
    flat250 = db.Column(db.String(20))
    flat300 = db.Column(db.String(20))
    flat350= db.Column(db.String(20))
    flat400 = db.Column(db.String(20))
    villa300 =db.Column(db.String(20))
    villa400 = db.Column(db.String(20))
    villa500 =db.Column(db.String(20))
    villa600 =db.Column(db.String(20))
    villa700 =db.Column(db.String(20))
    def delete(self):
        db.session.delete(self)
        db.session.commit()  
    def __init__(self,data):
        self.home120 = data['home120']
        self.home200 = data['home200']
        self.home250 =data['home250']
        self.home300 =data['home300']
        self.home350 =data['home350']
        self.home400 =data['home400']
        self.flat120 = data['flat120']
        self.flat200 = data['flat200']
        self.flat250 = data['flat250']
        self.flat300 = data['flat300']
        self.flat350= data['flat350']
        self.flat400 = data['flat400']
        self.villa300 =data['villa300']
        self.villa400 = data['villa400']
        self.villa500 =data['villa500']
        self.villa600 =data['villa600']
        self.villa700 =data['villa700']
    def create(self):
        db.session.add(self)
        db.session.commit()
