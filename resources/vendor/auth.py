import datetime
import email
import random
from marshmallow import Schema, ValidationError , fields
from marshmallow.validate import Length
from flask import jsonify, make_response, request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from database.vendor.schema import*
from database.vendor.model import*
from flask_jwt_extended import create_access_token
from resources.errors import VendorAlreadyExistError,VendorNotAuthorizedError,VendorNotFoundError
class VendorSignupApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            vendor_schema = VendorSchema()
            vendor = vendor_schema.load(data)
            vendor = Vendor(vendor)
            password = generatePassword(vendor.phone)
            vendor.password = password
            vendor.hash_password()
            vendor.create()
            result = vendor_schema.dump(vendor)
            result['password']= password
            return make_response(jsonify({"vendor": result}),200)
        except IntegrityError:
            raise VendorAlreadyExistError
        except Exception as e :
            raise Exception

class VendorLoginApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            validation = validateLogin()
            validation.load(data)
            vendor =  Vendor.query.filter(Vendor.phone==data['phone']).first()
            if not vendor:
                raise VendorNotFoundError
            authorized = vendor.check_password(data['password'])
            if not authorized:
                raise VendorNotAuthorizedError
            expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=str(vendor.id), expires_delta=expires)
            user_schema = VendorSchema(only=('name','phone'))
            user_schema = user_schema.dump(vendor)
            user_schema['token']= access_token
            return make_response({'message':'Login Successfully','data':user_schema},200)
        except ValidationError as e :
            return {'message':'Missing required fields'}
        except VendorNotAuthorizedError:
            raise VendorNotAuthorizedError
        except VendorNotFoundError:
            raise VendorNotFoundError
        except Exception as e:
            raise Exception
class validateLogin(Schema):
    phone = fields.String(required=True,validate=Length(min=11,max=13))
    password = fields.String(required=True,validate=Length(min=8))
def generatePassword(phone):
    return phone+"@"+str(random.randrange(10000,99999))