
import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource
from marshmallow import ValidationError
from database.order.schema import*
from database.order.model import*
from database.user.model import User
from database.vendor.model import Vendor
from database.area.model import Area
from resources.jwt_func import jwt_needed
from flask_jwt_extended import get_jwt_identity
from resources.errors import ServiceNotProvidedError, SchemaValidationError,UserNotFoundError,VendorNotFoundError
class OrderApi(Resource):
    @jwt_needed
    def post(self):
        try:
            data = request.get_json()
            id = get_jwt_identity()
            user = User.query.get(id)
            vendor = Vendor.query.get(data['ordered_to'])
            if not user :
                raise UserNotFoundError
            if not vendor:
                raise VendorNotFoundError
            if not checlService(data):
                raise ServiceNotProvidedError
            address = [data['order_address']['governerate'],data['order_address']['city'],data['order_address']['district'],data['order_address']['building']]
            address = '/'.join(address)
            data['order_address']=address
            order_schema = OrderSchema()
            order = order_schema.load(data)
            order = Order(order)
            order.ordered_at = datetime.datetime.now()
            order.ordered_by = id
            
            order.create()
            result = order_schema.dump(order)
            return make_response(jsonify({"order": result}),200)
        except (ValidationError,KeyError):
            raise SchemaValidationError
        except Exception as e:
            raise e

def checlService(data):
    if data['service']=='cleaning':
        return True
class CancleOrderApi(Resource):
    @jwt_needed
    def post(self):
        try:
            id = get_jwt_identity()
            data = request.get_json()
            order = Order.query.filter(Order.id==data['order_id'],Order.ordered_by==id).first()
            if not order:
                return {'message':'Order not found'},400
            else:
                order.order_status = 'canceled'
                order.create()
                return {'message':'Order canceled successfully'},200
        except KeyError :
            raise SchemaValidationError
        except  Exception as e :
            raise e
class RateOrderApi(Resource):
    @jwt_needed
    def post(self):
        try:
            id = get_jwt_identity()
            data = request.get_json()
            order = Order.query.filter(Order.id==data['order_id'],Order.ordered_by==id).first()
            if not order:
                return {'message':'Order not found'},400
            else:
                order.rate = data['order_rate']
                order.create()
                vendor = Vendor.query.get(order.ordered_to)
                rate = 0
                c=0
                for i in vendor.orders:
                    if i.rate != None:
                        c+=1
                        rate += i.rate 
                vendor.rate = rate/c
                vendor.create()
                return {'message':'Order rate saved successfully'},200
        except KeyError :
            raise SchemaValidationError
        except  Exception as e :
            raise e