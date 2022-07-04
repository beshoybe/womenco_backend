from email.policy import default
from marshmallow_sqlalchemy import SQLAlchemySchema
from database.order.model import Order
from marshmallow import fields
from app import db


class OrderSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Order
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    service= fields.String(required=True)
    ordered_at = fields.DateTime()
    ordered_by = fields.Number()
    ordered_to = fields.Number(required=True)
    order_price = fields.Float(required=True)
    order_address = fields.String(required=True)
    order_details = fields.String()
    order_status = fields.String()
    order_datetime = fields.DateTime()
    rate = fields.Number()