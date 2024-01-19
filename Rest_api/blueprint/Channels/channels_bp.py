from flask import Blueprint
from flask_restful import Api

channel_bp: Blueprint = Blueprint("channel_bp", __name__)
channels_bp: Blueprint = Blueprint("channels_bp", __name__)

channel_api: Api = Api(channel_bp)
channels_api: Api = Api(channels_bp)


