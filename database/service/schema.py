from marshmallow_sqlalchemy import SQLAlchemySchema
from database.service.model import *
from marshmallow import fields
from app import db


class CleaningSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Cleaning
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    home120 = fields.String()
    home200 = fields.String()
    home250 =fields.String()
    home300 =fields.String()
    home350 =fields.String()
    home400 =fields.String()
    flat120 = fields.String()
    flat200 = fields.String()
    flat250 = fields.String()
    flat300 = fields.String()
    flat350= fields.String()
    flat400 = fields.String()
    villa300 =fields.String()
    villa400 = fields.String()
    villa500 =fields.String()
    villa600 =fields.String()
    villa700 =fields.String()

