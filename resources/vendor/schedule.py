from flask import make_response, request
from database.schedule.model import*
from database.schedule.schema import*
from flask_restful import Resource
from resources.jwt_func import jwt_needed
from flask_jwt_extended import get_jwt_identity
from resources.errors import SchemaValidationError,DayAlreadyExistsError,DayNameError
class VendorSchedule(Resource):

    @jwt_needed
    def post(self):
        try:
            id = get_jwt_identity()
            data = request.get_json()
            if ('day' not in data) | ('start_time'not in data)| ('end_time' not in data):
                raise SchemaValidationError
            schedule = Schedule.query.get(id)
            if not schedule :
                schedule = Schedule()
                schedule.id = id
                schedule.create()
            if data['day'] not in days :
                raise DayNameError
            status  = addDay(data,schedule)
            if status :
                schedule.create()
                return {'message':"Day is added successfully"},200
            else:
                raise DayAlreadyExistsError
        except SchemaValidationError:
            raise SchemaValidationError
        except DayAlreadyExistsError:
            raise DayAlreadyExistsError
        except DayNameError :
            raise DayNameError
        except Exception as e:
            raise Exception
    @jwt_needed
    def put(self):
        id = get_jwt_identity()
        data = request.get_json()
        if ('day' not in data) | ('start_time'not in data)| ('end_time' not in data):
            raise SchemaValidationError
        schedule = Schedule.query.get(id)
        if not schedule :
            schedule = Schedule()
            schedule.id = id
            schedule.create()
        if data['day'] not in days :
            return {'message':'Day invalid'},400
        status  = editDay(data,schedule)
        if status :
            schedule.create()
            return {'message':"Day is edit successfully"},200
        else:
            return {'message':'Day is not added before'},400
    @jwt_needed
    def delete(self):
        id = get_jwt_identity()
        data = request.get_json()
        if ('day' not in data):
            raise SchemaValidationError
        schedule = Schedule.query.get(id)
        if not schedule :
            schedule = Schedule()
            schedule.id = id
            schedule.create()
        if data['day'] not in days :
            return {'message':'Day invalid'},400
        status  = delDay(data,schedule)
        if status :
            schedule.create()
            return {'message':"Day is deleted successfully"},200
        else:
            return {'message':'Day is not added before'},400
    @jwt_needed
    def get(self):
        id = get_jwt_identity()
        schedule_schema = ScheduleSchema(exclude = ('id',))
        schedule = Schedule.query.get(id)
        if not schedule :
            schedule = Schedule()
            schedule.id = id
            schedule.create()
        return make_response({'schedule':schedule_schema.dump(schedule)},200)

        

days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
def addDay(data,schedule):
    status = True
    if data['day']=='sunday': 
        if schedule.sun_start == None:
            schedule.sun_start = data['start_time']
            schedule.sun_end = data['end_time']
        else:
            status = False
    if data['day']=='monday': 
        if schedule.mon_start == None:
            schedule.mon_start = data['start_time']
            schedule.mon_end = data['end_time']
        else:
            status = False
    if data['day']=='tuesday': 
        if schedule.tue_start == None:
            schedule.tue_start = data['start_time']
            schedule.tue_end = data['end_time']
        else:
            status = False
    if data['day']=='wednesday': 
        if schedule.wed_start == None:
            schedule.wed_start = data['start_time']
            schedule.wed_end = data['end_time']
        else:
            status = False
    if data['day']=='thursday': 
        if schedule.thu_start == None:
            schedule.thu_start = data['start_time']
            schedule.thu_end = data['end_time']
        else:
            status = False
    if data['day']=='friday': 
        if schedule.fri_start == None:
            schedule.fri_start = data['start_time']
            schedule.fri_end = data['end_time']
        else:
            status = False
    if data['day']=='saturday': 
        if schedule.sat_start == None:
            schedule.sat_start = data['start_time']
            schedule.sat_end = data['end_time']
        else:
            status = False
    return status
def editDay(data,schedule):
    status = True
    if data['day']=='sunday': 
        if schedule.sun_start != None:
            schedule.sun_start = data['start_time']
            schedule.sun_end = data['end_time']
        else:
            status = False
    if data['day']=='monday': 
        if schedule.mon_start != None:
            schedule.mon_start = data['start_time']
            schedule.mon_end = data['end_time']
        else:
            status = False
    if data['day']=='tuesday': 
        if schedule.tue_start != None:
            schedule.tue_start = data['start_time']
            schedule.tue_end = data['end_time']
        else:
            status = False
    if data['day']=='wednesday': 
        if schedule.wed_start != None:
            schedule.wed_start = data['start_time']
            schedule.wed_end = data['end_time']
        else:
            status = False
    if data['day']=='thursday': 
        if schedule.thu_start != None:
            schedule.thu_start = data['start_time']
            schedule.thu_end = data['end_time']
        else:
            status = False
    if data['day']=='friday': 
        if schedule.fri_start != None:
            schedule.fri_start = data['start_time']
            schedule.fri_end = data['end_time']
        else:
            status = False
    if data['day']=='saturday': 
        if schedule.sat_start != None:
            schedule.sat_start = data['start_time']
            schedule.sat_end = data['end_time']
        else:
            status = False
    return status
def delDay(data,schedule):
    status = True
    if data['day']=='sunday': 
        if schedule.sun_start != None:
            schedule.sun_start = None
            schedule.sun_end = None
        else:
            status = False
    if data['day']=='monday': 
        if schedule.mon_start != None:
            schedule.mon_start = None
            schedule.mon_end = None
        else:
            status = False
    if data['day']=='tuesday': 
        if schedule.tue_start != None:
            schedule.tue_start = None
            schedule.tue_end = None
        else:
            status = False
    if data['day']=='wednesday': 
        if schedule.wed_start != None:
            schedule.wed_start = None
            schedule.wed_end = None
        else:
            status = False
    if data['day']=='thursday': 
        if schedule.thu_start != None:
            schedule.thu_start = None
            schedule.thu_end =None
        else:
            status = False
    if data['day']=='friday': 
        if schedule.fri_start != None:
            schedule.fri_start = None
            schedule.fri_end = None
        else:
            status = False
    if data['day']=='saturday': 
        if schedule.sat_start != None:
            schedule.sat_start = None
            schedule.sat_end = None
        else:
            status = False
    return status