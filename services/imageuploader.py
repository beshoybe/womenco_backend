import imp
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from resources.jwt_func import jwt_needed
from database.vendor.model import Vendor
from database.user.model import User
from resources.errors import*
image_path = "static/images/"
baseurl = "http://www.api.womencoeg.com/static/images/"
class VendorProfileImage(Resource):
    @jwt_needed
    def post(self):
        try:
            vendor_id = get_jwt_identity()
            vendor = Vendor.query.get(vendor_id)
            file_to_upload = request.files['file']
            ext = ext_check(file_to_upload.filename)
            if ext:
                path = image_path+'vendor/'+vendor_id+ext
                file_to_upload.save(path)
                vendor.photo = baseurl+'vendor/'+vendor_id+ext
                vendor.create()
            return {'message':'image saved successfully'},200
        except Exception as e:
            raise e
class UserProfileImage(Resource):
    @jwt_needed
    def post(self):
        try:
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            file_to_upload = request.files['file']
            ext = ext_check(file_to_upload.filename)
            if ext:
                path = image_path+'user/'+user_id+ext
                file_to_upload.save(path)
                user.photo = baseurl+'user/'+user_id+ext
                user.create()
            return {'message':'image saved successfully'},200
        except Exception as e:
            raise e
allowed_ext = ['.png','.jpg','.gif','.webp','.jpeg']
def ext_check(img_name):
    for i in allowed_ext:
        if i in img_name:
            return i

