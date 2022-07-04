import imp
from flask import request
from flask_restful import Resource
from resources.jwt_func import jwt_needed
from flask_jwt_extended import get_jwt_identity
from database.order.model import Order
from database.order.schema import OrderSchema
class VendorOrderStatusApi(Resource):
    @jwt_needed
    def post(self):
        id = get_jwt_identity()
        data = request.get_json()
        order = Order.query.filter(Order.id==data['order_id'],Order.ordered_to==id).first()
        if not order:
            return {'message':'order not found'},400
        if data['status']=='accept':
            order.order_status = 'accepted'
        elif data['status']=='decline':
            order.order_status = 'declined'
        else:
            return {'message':'Wrong status'},400
        order.create()
        return {'message':'order %s successfully'%(data['status'])},200
class VendorOrderFinishApi(Resource):
    @jwt_needed
    def post(self):
        id = get_jwt_identity()
        data = request.get_json()
        order = Order.query.filter(Order.id==data['order_id'],Order.ordered_to==id).first()
        if not order:
            return {'message':'order not found'},400
        if data['status']=='finish':
            order.order_status = 'finished'
        else:
            return {'message':'Wrong status'},400
        order.create()
        return {'message':'order %s successfully'%(data['status'])},200
class VendorOrderGetApi(Resource):
    @jwt_needed
    def get(self):
        id = get_jwt_identity()
        order_schema = OrderSchema(many=True)
        order = Order.query.filter(Order.ordered_to==id)
        if not order:
            return {'message':'order not found'},400

        order= order_schema.dump(order)
        return {'orders':order},200