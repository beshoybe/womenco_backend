from app import db
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash, check_password_hash
from database.order.model import Order
class Vendor(db.Model):
    __tablename__ = "vendor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    namearabic = db.Column(db.String(20))
    password = db.Column(db.String(100))
    phone = db.Column(db.String(14),unique=True)
    orders = relationship('Order')
    areas = relationship('VendorArea')
    photo = db.Column(db.String(150),default = '')
    cleaning = relationship('Cleaning')
    schedule = relationship('Schedule')
    rate = db.Column(db.Integer,default = 0)
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,data):
        self.name = data['name']
        self.phone = data['phone']
        self.namearabic = data['namearabic']
    def __repr__(self):
        return '' % self.id