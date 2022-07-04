
from resources.user.auth import*
from resources.vendor.auth import*
from resources.user.order import*
from resources.admin.area import*
from resources.vendor.area import*
from resources.vendor.service import*
from resources.vendor.schedule import*
from resources.user.search import*
from resources.vendor.order import*
from services.imageuploader import *
def initialize_routes(api):
    api.add_resource(UserSignupApi, '/user/signup')
    api.add_resource(UserLoginApi, '/user/login')
    api.add_resource(UserVerifyApi, '/user/verify')
    api.add_resource(SendOtp, '/sendotp')
    api.add_resource(VendorSignupApi, '/admin/vendorsignup')
    api.add_resource(AreaApi, '/admin/area')
    api.add_resource(VendorLoginApi, '/vendor/login')
    api.add_resource(VendorAreaApi, '/vendor/area')
    api.add_resource(VendorServiceApi, '/vendor/service')
    api.add_resource(VendorSchedule, '/vendor/schedule')
    api.add_resource(VendorOrderStatusApi, '/vendor/order/status')
    api.add_resource(VendorOrderFinishApi, '/vendor/order/finish')
    api.add_resource(VendorOrderGetApi, '/vendor/order')
    api.add_resource(Search, '/user/search')
    api.add_resource(OrderApi, '/user/order/new')
    api.add_resource(CancleOrderApi, '/user/order/cancle')
    api.add_resource(RateOrderApi, '/user/order/rate')
    api.add_resource(VendorProfileImage, '/vendor/profileimage/')
    api.add_resource(UserProfileImage, '/user/profileimage/')
    api.add_resource(GetUserData, '/user')
    api.add_resource(ForgetPasswordUser, '/user/forget')
    api.add_resource(ChangePassbyOtp, '/user/passreset')
    api.add_resource(UpdateUserData, '/user/update')
    api.add_resource(vendorGet, '/vendor')



