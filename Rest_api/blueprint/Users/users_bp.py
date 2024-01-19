from flask import Blueprint
from flask_restful import Api

Users_bp: Blueprint = Blueprint("Users_bp", __name__)
User_bp: Blueprint = Blueprint("User_bp", __name__)

users_api: Api = Api(Users_bp)
user_api: Api = Api(User_bp)
    


