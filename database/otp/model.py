import email
from app import db

class Otp(db.Model):
    __tablename__ = "otp"
    otp = db.Column(db.String(5))
    email = db.Column(db.String(50),primary_key=True)
    def __init__(self,data):
        self.otp = data['otp']
        self.email = data['email']
    def create(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()