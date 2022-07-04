from app import db
class Schedule(db.Model):
    __tablename__ = "vendor_schedule"
    id  = db.Column(db.Integer,db.ForeignKey('vendor.id'),primary_key= True)
    sun_start = db.Column(db.Time)
    sun_end = db.Column(db.Time)
    mon_start = db.Column(db.Time)
    mon_end = db.Column(db.Time)
    tue_start = db.Column(db.Time)
    tue_end = db.Column(db.Time)
    wed_start = db.Column(db.Time)
    wed_end = db.Column(db.Time)
    thu_start = db.Column(db.Time)
    thu_end = db.Column(db.Time)
    fri_start = db.Column(db.Time)
    fri_end = db.Column(db.Time)
    sat_start = db.Column(db.Time)
    sat_end = db.Column(db.Time)
    def create(self):
        db.session.add(self)
        db.session.commit()