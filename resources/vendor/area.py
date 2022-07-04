from flask import make_response, request
from flask_restful import Resource
from database.area.model import VendorArea,Area
from database.area.schema import VendorAreaSchema
from resources.jwt_func import jwt_needed

from flask_jwt_extended import get_jwt_identity
class VendorAreaApi(Resource):
    @jwt_needed
    def post(self):
        data = request.get_json()
        id = get_jwt_identity()
        vendorarea_schema = VendorAreaSchema()
        data = vendorarea_schema.load(data)
        area = Area.query.filter(Area.city==data['city']).first()
        if not area:
            return {'message':'Area not found'},400
        vendorarea = VendorArea(data)
        vendorarea.added_by = eval(id)
        vendorarea.create()
        return make_response({'message':'Area add successfully'},200)
    @jwt_needed
    def delete(self):
        data = request.get_json()
        id = get_jwt_identity()
        area = VendorArea.query.filter(VendorArea.city==data['city'],VendorArea.added_by==eval(id)).first()
        if not area:
            return {'message':'Area is not found'},401
        area.delete()
        return make_response({'message':'Area Delete successfully'},200)
    @jwt_needed
    def get(self):
        area_schema = VendorAreaSchema(many=True)
        id = get_jwt_identity()
        area = VendorArea.query.filter(VendorArea.added_by==eval(id))
        for i in area :
            i.districts = eval(i.districts)
        area = area_schema.dump(area)
        return make_response({'data':area},200)

