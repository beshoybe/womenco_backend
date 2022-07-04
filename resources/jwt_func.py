import imp
from jwt.exceptions import DecodeError
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

from functools import wraps
def jwt_needed(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            verify_jwt_in_request(locations='headers')
        except (ValueError, DecodeError, TypeError, ):
            return  {'message':'Wrong or Expired Token'},401
        except NoAuthorizationError:
            return {
        'message':'Token is missing from headers'},401
        return func(*args, **kwargs)
    return decorator
