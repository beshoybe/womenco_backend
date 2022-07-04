from datetime import datetime
from operator import ge
import os
from webbrowser import get
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from resources.errors import errors


app = Flask(__name__)
os.environ['ENV_FILE_LOCATION']='./.env'
app.config.from_envvar('ENV_FILE_LOCATION')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://womemroe_womenco:12345678womenco@localhost:3306/womemroe_womenco'
db = SQLAlchemy(app,session_options={"autoflush": False})
bcrypt = Bcrypt(app)
api = Api(app,errors=errors)
mail = Mail(app)
jwt = JWTManager(app) 
from database.order.model import*
from database.order.schema import*
from database.user.model import*
from database.user.schema import*
from resources.routes import initialize_routes
initialize_routes(api)
db.create_all()
@app.route('/')
def new():
    return 'Hello'
