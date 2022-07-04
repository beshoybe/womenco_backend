from datetime import datetime,timedelta
import imp
from time import time
from flask import request
from flask_restful import Resource
from resources.jwt_func import jwt_needed
from database.vendor.model import Vendor
from database.vendor.schema import VendorSchema
from database.area.model import VendorArea
from database.service.model import*
from database.schedule.model import Schedule 
from database.order.model import Order
class Search(Resource):
    def post(self):
        data = request.get_json()
        vendor_schema = VendorSchema(many =True,only=(data['service'],'id','name','phone','photo','orders','rate','namearabic'))
        searchdatetime = data['date']+' '+data['time']
        searchdatetime  = datetime.strptime(searchdatetime,'%Y-%m-%d %H:%M:%S')
        day = daycheck(searchdatetime.weekday())
        print(searchdatetime+timedelta(hours=3))
        now = datetime.now()
        service = serviceCheck(data)
        vendors = Vendor.query.join(VendorArea).join(Schedule).filter(data['time']<=day[1],
                                    data['time']>=day[0],
                                 service,
                                    VendorArea.governerate ==data['address']['governerate'],
                                    VendorArea.city == data['address']['city'],)
        vendors = vendor_schema.dump(vendors)                            
        for i in vendors:
            for j in i['orders']:
                if j['order_status'] == 'canceled':
                    break
                if j['order_status'] == 'finished':
                    break
                if (searchdatetime-timedelta(hours=3)<datetime.strptime(j['order_datetime'].replace('T',' '),'%Y-%m-%d %H:%M:%S')<searchdatetime)|(searchdatetime+timedelta(hours=3)>datetime.strptime(j['order_datetime'].replace('T',' '),'%Y-%m-%d %H:%M:%S')>searchdatetime):
                    if i in vendors:
                        vendors.pop(vendors.index(i))

        return {'data':vendors}
class vendorGet(Resource):
    @jwt_needed
    def post(self):
        data = request.get_json()
        vendor = Vendor.query.get(data['id'])
        vendor_schema = VendorSchema()
        return{'vendor':vendor_schema.dump(vendor)}
        
def serviceCheck(data):
    if data['service']=='cleaning':
        return Vendor.cleaning.any()
def daycheck(date):
    if date == 5:
        return (Schedule.sun_start,Schedule.sun_end)
    elif date == 6:
        return (Schedule.mon_start,Schedule.mon_end)
    elif date == 0:
        return (Schedule.tue_start,Schedule.tue_end)
    elif date == 1:
        return (Schedule.wed_start,Schedule.wed_end)
    elif date == 2:
        return (Schedule.thu_start,Schedule.thu_end)
    elif date == 3:
        return (Schedule.fri_start,Schedule.fri_end)
    elif date == 4:
        return (Schedule.sat_start,Schedule.sat_end)