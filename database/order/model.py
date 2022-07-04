
from app import db
class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(20))
    ordered_at = db.Column(db.DateTime)
    ordered_by = db.Column(db.Integer,db.ForeignKey('user.id'))
    ordered_to = db.Column(db.Integer,db.ForeignKey('vendor.id'))
    order_price = db.Column(db.Float)
    order_address = db.Column(db.String(1000))
    order_status = db.Column(db.String(10),default = 'awaiting')
    order_details= db.Column(db.String(1000))
    rate = db.Column(db.Integer)
    order_datetime = db.Column(db.DateTime)
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,data):
        self.service = data['service']
        self.ordered_to = data['ordered_to']
        self.order_price = data['order_price']
        self.order_address = data['order_address']
        self.order_details = data['order_details']
        self.order_datetime = data['order_datetime']
    def __repr__(self):
        return '' % self.id