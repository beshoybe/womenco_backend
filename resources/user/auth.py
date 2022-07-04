import datetime
import random
from flask import jsonify, make_response, request
from flask_restful import Resource
from resources.jwt_func import jwt_needed
from marshmallow import Schema, ValidationError,fields
from database.user.schema import*
from flask_jwt_extended import get_jwt_identity
from database.user.model import*
from flask_jwt_extended import create_access_token
from database.otp.model import*
from services.mail_Service import*
from sqlalchemy.exc import IntegrityError
from resources.errors import UserAlreadyExistError,UserNotAuthorizedError,UserNotFoundError,UserNotVerifiedError,SchemaValidationError
class UserSignupApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            user_schema = UserSchema()
            user = user_schema.load(data)
            user = User(user)
            user.hash_password()
            user.create()
            return make_response(jsonify({"message":'User signup succesfully'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
            raise UserAlreadyExistError
        except Exception as e:
            raise Exception
class UserLoginApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            if ('email' not in data) | ('password' not in data):
                raise ValidationError
            user =  User.query.filter(User.email==data['email']).first()
            if not user:
                raise UserNotFoundError
            authorized = user.check_password(data['password'])
            if not authorized:
                raise UserNotAuthorizedError
            expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            user_schema = UserSchema(only=('name','email','id','verified'))
            user_schema = user_schema.dump(user)
            user_schema['token']= access_token
            return make_response({'message':'Login Succesfully','data':user_schema},200)
        except UserNotFoundError:
            raise UserNotFoundError
        except UserNotAuthorizedError:
            raise UserNotAuthorizedError
        except UserNotVerifiedError:
            raise UserNotVerifiedError
        except Exception as e:
            raise e
class UserVerifyApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            otp = Otp.query.get(data['email'])
            if not otp:
                raise UserNotFoundError
            if otp.otp == data['otp']:
                user =  User.query.filter(User.email==data['email']).first()
                user.verified = True
                user.create()
                otp.delete()
                return {'message':'Verified Successfully'},200
            else:
                return {'message':'Wrong OTP'},400
        except UserNotFoundError:
            raise UserNotFoundError
        except Exception as e :
            raise Exception

class SendOtp(Resource):
    def post(self):
        data = request.get_json()
        otp = Otp.query.get(data['email'])
        myotp = str(random.randrange(10000,99999))
        if not otp:
            otp =Otp({'otp':myotp,'email':data['email']})
        else:
            otp.otp = myotp
        otp.create()
        send_email('[WomenCo] Verify your account',
            sender=('WomenCo','app@womencoeg.com'),
            recipients=[data['email']],
            text_body=render_template('otp.txt',otp=otp.otp),
            html_body=render_template('otp.html',otp=otp.otp))
        return {'message':'otp send successfully','otp':otp.otp},200

class GetUserData(Resource):
    @jwt_needed
    def get(self):
        try:
            id = get_jwt_identity()
            user = User.query.get(id)
            user_schema = UserSchema()
            if not user:
                raise UserNotFoundError
            user = user_schema.dump(user)
            return {'data':user},200
        except Exception as e:
            raise e
class ForgetPasswordUser(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.email==data['email']).first()
        otp = Otp.query.get(data['email'])
        myotp = str(random.randrange(10000,99999))
        if not user:
            return {'message':'Invalid email, Please check your mail'},400
        if not otp:
            otp =Otp({'otp':myotp,'email':data['email']})
        else:
            otp.otp = myotp
        otp.create()
        send_email('Password Reset',
            sender=('WomenCo','app@womencoeg.com'),
            recipients=[data['email']],
            text_body=render_template('forgetpass.txt',otp=otp.otp),
            html_body=render_template('forgetpass.html',otp=otp.otp))
        return {'message':'otp send successfully','otp':otp.otp},200
class ChangePassbyOtp(Resource):
    def post(self):
        try:
            data = request.get_json()
            otp = Otp.query.get(data['email'])
            if not otp:
                return {'message':'Wrong otp'},400
            if otp.otp == data['otp']:
                user =  User.query.filter(User.email==data['email']).first()
                user.password = data['password']
                user.hash_password()
                user.create()
                otp.delete()
                return {'message':'Verified Successfully'},200
            else:
                return {'message':'Wrong OTP'},400
        except UserNotFoundError:
            raise UserNotFoundError
        except Exception as e :
            raise Exception
class UpdateUserData(Resource):
    @jwt_needed
    def post(self):
        try:
            id  = get_jwt_identity()
            data = request.get_json()
            user = User.query.get(id)
            user.email=data['email']
            user.name = data['name']
            user.password = data['password']
            user.phone = data['phone']
            user.hash_password()
            user.create()
            return make_response(jsonify({"message":'User Updated Successfully'}),200)
        except KeyError:
            raise SchemaValidationError
        except IntegrityError as e:
            raise UserAlreadyExistError
        except Exception as e:
            raise Exception