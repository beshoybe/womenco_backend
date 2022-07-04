
class UserAlreadyExistError(Exception):
    pass
class VendorAlreadyExistError(Exception):
    pass
class UserNotAuthorizedError(Exception):
    pass
class VendorNotAuthorizedError(Exception):
    pass
class UserNotFoundError(Exception):
    pass
class VendorNotFoundError(Exception):
    pass
class UserNotVerifiedError(Exception):
    pass
class SchemaValidationError(Exception):
    pass
class DayAlreadyExistsError(Exception):
    pass
class DayNameError(Exception):
    pass
class ServiceAlreadyExistsError(Exception):
    pass
class ServiceNotProvidedError(Exception):
    pass
class AreaAlreadyExistsError(Exception):
    pass
errors = {
    'UserAlreadyExistError':{
        'message':'User with given email or phone is already exists',
        'status':400
    },
    'VendorAlreadyExistError':{
        'message':'Vendor with given phone is already exists',
        'status':400
    },
    'UserNotAuthorizedError':{
        'message':'Password is wrong',
        'status':400
    },
    'VendorNotAuthorizedError':{
        'message':'Password is wrong',
        'status':400
    },
    'UserNotFoundError':{
        'message':'User with provided email is not found',
        'status':400
    },
    'UserNotVerifiedError':{
        'message':'User with provided email is not verified',
        'status':400
    },
    'SchemaValidationError':{
        'message':'The request missing required fields, or wrong data types',
        'status':400
    },

    'DayAlreadyExistsError':{
        'message':'Day is added before',
        'status':400
    },
    'DayNameError':{
        'message':'Day is invalid',
        'status':400
    },
    'ServiceAlreadyExistsError':{
        'message':'The Service is added before',
        'status':400
    },
    'ServiceNotProvidedError':{
        'message':'Service is not provided'
    },
    'AreaAlreadyExistsError':{
        'message':'Area is added before',
        'status':400
    }
}