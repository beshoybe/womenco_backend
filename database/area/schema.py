from marshmallow_sqlalchemy import SQLAlchemySchema
from database.area.model import Area
from marshmallow import fields
from app import db


class AreaSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Area
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    governerate = fields.String(required=True)
    city = fields.String(required=True)
    arabicgovernerate = fields.String(required=True)
    arabiccity = fields.String(required=True)
class VendorAreaSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Area
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    governerate = fields.String(required=True)
    city = fields.String(required=True)
    added_by = fields.Number()
    arabicgovernerate = fields.String(required=True)
    arabiccity = fields.String(required=True)