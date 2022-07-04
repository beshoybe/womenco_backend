
import imp
from flask import make_response, request
from flask_restful import Resource
from database.service.model import*
from database.service.schema import*
from database.vendor.model import Vendor
from database.vendor.schema import VendorSchema
from resources.jwt_func import jwt_needed
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.exc import IntegrityError
from resources.errors import ServiceAlreadyExistsError,ServiceNotProvidedError,VendorNotFoundError
class VendorServiceApi(Resource):
    @jwt_needed
    def post(self):
        try:
            id = get_jwt_identity()
            data = request.get_json()
            service = create_service(data)
            if not service:
                raise ServiceNotProvidedError
            else:
                service.id = id
                service.create()
            return make_response({'message':'Service Added Successfully'},200)
        except IntegrityError:
            raise ServiceAlreadyExistsError
        except Exception as e:
            raise e
    @jwt_needed
    def put(self):
        try:
            id = get_jwt_identity()
            data = request.get_json()
            service = get_service(data,id)
            if not service:
                raise ServiceNotProvidedError
            else:
                update_service(data,service,id)
            return make_response({'message':'Service Edit Successfully'},200)
        except IntegrityError:
            return ServiceAlreadyExistsError
        except Exception as e:
            raise e
    @jwt_needed
    def delete(self):
        try:
            id = get_jwt_identity()
            data = request.get_json()
            service = get_service(data,id)
            if not service:
                raise ServiceNotProvidedError
            else:
                service.delete()
            return make_response({'message':'Service Deleted Successfully'},200)
        except Exception as e:
            raise e
    @jwt_needed
    def get(self):
        try:
            id = get_jwt_identity()
            vendor = Vendor.query.get(id)
            if not vendor:
                raise VendorNotFoundError
            else:
                vendor_schema= VendorSchema(only= ('cleaning',))
                vendor=vendor_schema.dump(vendor)
            return make_response({'services':vendor},200)
        except Exception as e:
            raise Exception
def update_service(data,service,id):
    service.delete()
    service = create_service(data)
    service.id = id
    service.create()
def get_service(data,id):
    service = None
    if data['service_type']=='cleaning':
        service = Cleaning.query.get(id)
    return service  
def create_service(data):
    service = None
    if data['service_type']=='cleaning':
        data.pop('service_type')
        schema = CleaningSchema()
        service = schema.load(data)
        service = Cleaning(service)
    return service
        