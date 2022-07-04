from marshmallow_sqlalchemy import SQLAlchemySchema
from database.user.model import User
from marshmallow import fields
from app import db

class UserSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = User
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    phone = fields.String(required=True)
    photo = fields.String()
    verified = fields.Boolean()
    orders = fields.Nested('OrderSchema',many=True)