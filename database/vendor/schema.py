from database.vendor.model import Vendor
from database.order.schema import OrderSchema
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app import db
class VendorSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Vendor
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    namearabic = fields.String(required=True)
    name = fields.String(required=True)
    phone = fields.String(required=True)
    photo = fields.String()
    orders = fields.Nested('OrderSchema',many=True)
    cleaning = fields.Nested('CleaningSchema',exclude=('id',),many=True)
    schedule = fields.Nested('ScheduleSchema',exclude=('id',),many=True)
    rate = fields.Number()