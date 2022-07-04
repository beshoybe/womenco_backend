from app import db
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash, check_password_hash
from database.order.model import Order
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    phone = db.Column(db.String(14),unique=True)
    orders = relationship('Order',lazy='dynamic')
    photo = db.Column(db.String(150),default = '')
    verified = db.Column(db.Boolean,default = False)
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
        self.email = data['email']
        self.password = data['password']
        self.phone = data['phone']
    def __repr__(self):
        return '' %self.orders