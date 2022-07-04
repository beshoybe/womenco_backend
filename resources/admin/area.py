

from flask import make_response, request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from database.area.schema import*
from database.area.model import*
from resources.errors import AreaAlreadyExistsError
class AreaApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            area_schema = AreaSchema()
            area = area_schema.load(data)
            area = Area(area)
            area.create()
            return make_response({'message':'Area add successfully'},200)
        except IntegrityError :
            raise AreaAlreadyExistsError
    def delete(self):
        data = request.get_json()
        area = Area.query.filter(Area.city==data['city']).first()
        if not area:
            return {'message':'Area is not found'},400
        area.delete()
        return make_response({'message':'Area Delete successfully'},200)
    def get(self):
        ararea_schema = AreaSchema(many=True,only=('id','arabicgovernerate','arabiccity'))
        enarea_schema = AreaSchema(many=True,only=('id','governerate','city'))
        area = Area.query.all()
        ararea = ararea_schema.dump(area)
        enarea = enarea_schema.dump(area)
        return make_response({'arabic':ararea,'english':enarea},200)