from marshmallow_sqlalchemy import SQLAlchemySchema
from database.schedule.model import *
from marshmallow import fields
from app import db
class ScheduleSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Schedule
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    sun_start = fields.Time()
    sun_end = fields.Time()
    mon_start = fields.Time()
    mon_end = fields.Time()
    tue_start = fields.Time()
    tue_end = fields.Time()
    wed_start = fields.Time()
    wed_end = fields.Time()
    thu_start = fields.Time()
    thu_end = fields.Time()
    fri_start = fields.Time()
    fri_end = fields.Time()
    sat_start = fields.Time()
    sat_end = fields.Time()